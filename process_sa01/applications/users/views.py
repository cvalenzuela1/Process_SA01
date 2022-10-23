import datetime
import pandas as pd
from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView, View, TemplateView
from django.views.generic.edit import FormView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.conf import settings

from .models import Estado, Usuario, Rol, Tarea, Persona, TareaPersona
from .forms import GestionarTareaForm, LoginForm
from .functions import *


# Create your views here.
class Test1TemplateView(TemplateView):
    template_name = "users/test1.html"


class CountTareasSolicitadas(object):
    def get_context_data(self, **kwargs):
        context = super(CountTareasSolicitadas, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            persona_id = self.request.user.persona_id_persona.id_persona
            tareas_solicitadas = Tarea.objects.get_tareas_solicitadas()
            context["count_tareas_solicitadas"] = TareaPersona.objects.count_tareas_solicitadas_by_persona(persona_id, tareas_solicitadas)

        return context
    

def updateTarea(request):
    if request.method == "POST":
        id_tarea = request.POST.get("idTarea")
        if id_tarea != None:
            titulo_tarea = request.POST.get("tituloTarea")
            desc_tarea = request.POST.get("descTarea")
            etiqueta_tarea = request.POST.get("etiquetaTarea")
            fecha_inicio = request.POST.get("fInicio")
            fecha_termino = request.POST.get("fTermino")
            if  len(fecha_termino) > 0 and fecha_termino != None:
                f_inicio = pd.to_datetime(fecha_inicio, infer_datetime_format=True)
                f_termino = datetime.datetime.strptime(str(fecha_termino), '%Y-%m-%d')
                diff = f_termino.date() - f_inicio.date()
                diff_days = diff.days

                if diff_days > 0:
                    Tarea.objects.update_tarea_fields(id_tarea, titulo_tarea, desc_tarea, etiqueta_tarea, fecha_termino)
                    messages.success(request, f"Tarea actualizada correctamente")
                else:
                    messages.warning(request, f"Fecha de término debe ser mayor a la de inicio")
                    return HttpResponseRedirect(
                        reverse(
                            "app_users:tareas-detalle", 
                            kwargs={'pk': id_tarea}
                        )
                    )
            else:
                Tarea.objects.update_tarea_fields(id_tarea, titulo_tarea, desc_tarea, etiqueta_tarea, None)
                messages.success(request, f"Tarea actualizada correctamente")
                
            return HttpResponseRedirect(reverse("app_users:tareas-list"))
        else:
            messages.warning(request, "Ha ocurrido un problema al actualizar")
            return HttpResponseRedirect(reverse("app_users:tareas-list"))
    else:
        messages.error(request, "Ha ocurrido un error al actualizar")
        return HttpResponseRedirect(reverse("app_users:tareas-list"))


class TareaDetailView(CountTareasSolicitadas, LoginRequiredMixin, DetailView):
    template_name = "users/detalle_tareas.html"
    model = Tarea
    # context_object_name = "object_tarea"
    success_url = reverse_lazy("app_users:tareas-list")

    def get_context_data(self, **kwargs):
        context = super(TareaDetailView, self).get_context_data(**kwargs)
        tareaPersona = TareaPersona.objects.get_tarea_by_id(self.kwargs['pk'])
        for item in tareaPersona:
            context["tareaPersona"] = item.persona_id_persona
            break
        f_termino = Tarea.objects.get_fecha_termino(self.kwargs['pk'])
        diff_days = getDiffDaysTerminoCurrent(f_termino)
        context["diffDays"] = int(diff_days.days)

        return context


class GestionarTareaView(CountTareasSolicitadas, FormView):
    template_name = "users/tareas.html"
    form_class = GestionarTareaForm
    success_url = reverse_lazy("app_users:tareas-list")

    def get(self, request, *args, **kwargs):
        tipo_permiso = request.user.permisos_id_permiso.tipo_permiso
        if tipo_permiso != 'Gerente' and tipo_permiso != 'Funcionario Crear':
            messages.warning(request, "No posees los permisos necesarios para ingresar a la url")
            return HttpResponseRedirect(reverse("app_home:home"))
        return super(GestionarTareaView, self).get(request, *args, **kwargs)

    def form_valid(self, form):
        f_inicio = form.cleaned_data['fecha_inicio']
        f_termino = form.cleaned_data['fecha_termino']

        diff = getDiffDaysTerminoInicio(f_termino, f_inicio)
        diff_current = getDiffDaysTerminoCurrent(f_termino)
        diff_current_inicio = getDiffDaysCurrentInicio(f_inicio)

        estado_tarea = Estado.objects.get_estado("Activa")[0][0]

        if diff.days > 0 and diff_current.days > 0 and diff_current_inicio.days >= 0:
            Tarea.objects.create_tarea(
                form.cleaned_data['titulo_tarea'],
                form.cleaned_data['desc_tarea'],
                form.cleaned_data['fecha_inicio'],
                form.cleaned_data['fecha_termino'],
                form.cleaned_data['etiqueta'],
                porc_cumplimiento=0,
                estado_alterado=0,
                estado_id_estado=Estado(estado_tarea))
            
            messages.success(self.request, "Tarea creada correctamente")
            return super(GestionarTareaView, self).form_valid(form)
        else:
            messages.warning(self.request, "Fechas ingresadas son inválidas")
            return HttpResponseRedirect(reverse("app_users:tareas"))

    def form_invalid(self, form):
        messages.warning(self.request, "Fechas ingresadas tienen un formato incorrecto")
        return HttpResponseRedirect(reverse("app_users:tareas"))


class TareaListView(CountTareasSolicitadas, LoginRequiredMixin, ListView):
    template_name = "users/list_tareas.html"
    paginate_by = 4
    model = Tarea
    context_object_name = "lista_tareas"

    def get(self, request, *args, **kwargs):
        tipo_permiso = request.user.permisos_id_permiso.tipo_permiso
        if tipo_permiso != 'Gerente' and tipo_permiso != 'Funcionario Crear':
            messages.warning(request, "No posees los permisos necesarios para ingresar a la url")
            return HttpResponseRedirect(reverse("app_home:home"))
        return super(TareaListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        username = self.request.user.nombre_usuario
        password = self.request.user.password_usuario
        rol_id = Usuario.objects.get_usuario_rol_id(username, password)[0][4]
        rol_nombre = Rol.objects.get_rol_nombre(rol_id)[0][1]
        self.request.session["rol_nombre"] = rol_nombre
        context = Tarea.objects.get_tareas_new_order(rol_nombre)
        
        return context


def tareaTerminar(request):
    if request.method == "POST":
        id_tarea = request.POST.get("tarea_id")
        if id_tarea != None:
            Tarea.objects.update_tarea(id_tarea, getCurrentDate())
            messages.success(request, "Tarea finalizada correctamente")
            return HttpResponseRedirect(reverse("app_users:tareas-list"))
        else:
            messages.warning(request, "Ha ocurrido un problema")
            return HttpResponseRedirect(reverse("app_users:tareas-list"))
    else:
        messages.error(request, "Ha ocurrido un error")
        return HttpResponseRedirect(reverse("app_users:tareas-list"))


def actualizarProgreso(request):
    if request.method == "POST":
        tarea  = Tarea.objects.get_fechas()

        if tarea:
            for item in tarea:
                f_inicio = item.fecha_inicio
                f_termino = item.fecha_termino
                tarea_id = item.id_tarea

                diff = getDiffDaysTerminoInicio(f_termino, f_inicio)
                diff_actual = getDiffDaysTerminoCurrent(f_termino)

                new_porc_cumplimiento = 100-(diff_actual.days * 100) / diff.days
                if item.estado_id_estado.id_estado == 2 or item.estado_id_estado.id_estado == 3:
                    if item.porc_cumplimiento == 100:
                        continue
                    if diff_actual.days <= 0:
                        Tarea.objects.update_porc_cumplimiento(100, tarea_id)
                        continue
                    elif diff_actual.days == diff.days:
                        new_porc_cumplimiento = 100-(diff_actual.days * 100) / diff.days
                    if new_porc_cumplimiento < 0:
                        Tarea.objects.update_porc_cumplimiento(0, tarea_id)
                    elif new_porc_cumplimiento > 0:
                        Tarea.objects.update_porc_cumplimiento(new_porc_cumplimiento, tarea_id)

            # Ejecución de procedimientos almacenados
            executeSPUpdateEstadoAlterado()
            executeSPUpdateEstadoTareas()
            # END ejecución de procedimientos almacenados
            messages.success(request, "Progresos actualizados correctamente")
            return HttpResponseRedirect(reverse("app_users:tareas-list"))
        else:
            messages.error(request, "Se ha producido un error al actualizar")
            return HttpResponseRedirect(reverse("app_home:tareas-list"))
    else:
        return HttpResponseRedirect(reverse("app_users:tareas-list"))


class AsignarResponsableView(CountTareasSolicitadas, LoginRequiredMixin, TemplateView):
    template_name = "users/asignar_responsable.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["lista_tareas"] = Tarea.objects.get_tareas_new_order2()
        context["lista_personas"] = Persona.objects.get_persona()
        return context

    def post(self, request):
        persona_id = request.POST.get("idPersona")
        contador_tareas = request.POST.get("tareaContador")
        lista_tareas = []
        for i in range(1, int(contador_tareas)+1):
            lista_tareas.append(request.POST.get(f"tarea{i}"))
        
        lista_objetos_tarea = {tarea_id: Tarea(tarea_id) for tarea_id in lista_tareas}
        Tarea.objects.update_tarea_estado(lista_tareas)
        TareaPersona.objects.create_tarea_persona(Persona(persona_id), lista_objetos_tarea)
        if int(contador_tareas) == 1:
            messages.success(request, f"Se ha asignado {contador_tareas} tarea a la persona con RUT \"{request.user.persona_id_persona.rut_persona}\"")
        elif int(contador_tareas) > 1:
            messages.success(request, f"Se han asignado {contador_tareas} tareas a la persona con RUT \"{request.user.persona_id_persona.rut_persona}\"")
        return HttpResponseRedirect(reverse("app_users:tareas-asignar"))


class TareasSolicitadasListView(CountTareasSolicitadas, LoginRequiredMixin, ListView):
    template_name = "users/list_tareas_solicitadas.html"
    paginate_by = 6
    model = TareaPersona
    context_object_name = "tareas_solicitadas"

    def get_queryset(self):
        persona_id = self.request.user.persona_id_persona.id_persona
        tareas_solicitadas = Tarea.objects.get_tareas_solicitadas()
        context = TareaPersona.objects.get_tareas_solicitadas_by_persona(persona_id, tareas_solicitadas)
        
        return context


def tareaAceptar(request):
    if request.method == "POST":
        id_tarea = request.POST.get("tarea_id")
        if id_tarea != None:
            Tarea.objects.update_tarea_solicitada(id_tarea)
            messages.success(request, "Tarea aceptada correctamente")
            return HttpResponseRedirect(reverse("app_users:tareas-list-solicitadas"))
        else:
            messages.warning(request, "Ha ocurrido un problema")
            return HttpResponseRedirect(reverse("app_users:tareas-list-solicitadas"))
    else:
        messages.error(request, "Ha ocurrido un error")
        return HttpResponseRedirect(reverse("app_users:tareas-list-solicitadas"))


def tareaRechazar(request):
    if request.method == "POST":
        id_tarea = request.POST.get("tarea_id")
        if id_tarea != None:
            Tarea.objects.update_tarea_rechazada(id_tarea)
            messages.success(request, "Tarea rechazada correctamente")
            return HttpResponseRedirect(reverse("app_users:tareas-list-solicitadas"))
        else:
            messages.warning(request, "Ha ocurrido un problema")
            return HttpResponseRedirect(reverse("app_users:tareas-list-solicitadas"))
    else:
        messages.error(request, "Ha ocurrido un error")
        return HttpResponseRedirect(reverse("app_users:tareas-list-solicitadas"))


def alertarAtrasos(request):
    if request.method == "POST":
        # Enviar mail a responsables de tareas atrasadas
        asunto = 'Alerta de atraso'
        mensaje = 'Título de tarea atrasada: '
        email_remitente = 'noneshater@gmail.com'
        tareas_atrasadas = Tarea.objects.get_tareas_atrasadas()
        oTareaPersona = TareaPersona.objects.get_tareas_by_tareas_atrasadas(tareas_atrasadas)
        for tarea_persona in oTareaPersona:
            for item in tarea_persona:
                email_destinatario = item.persona_id_persona.email_persona
                mensaje+=item.tarea_id_tarea.titulo_tarea
                send_mail(asunto, mensaje, email_remitente, [email_destinatario])
            mensaje = 'Título de tarea atrasada: '
        messages.success(request, "Alertas a tareas atrasadas enviadas correctamente")
        return HttpResponseRedirect(reverse("app_users:tareas-list"))
    else:
        return HttpResponseRedirect(reverse("app_users:tareas-list"))


class VerTareasAsignadasListView(CountTareasSolicitadas, ListView):
    template_name = "users/list_tareas_asignadas.html"
    model = TareaPersona
    context_object_name = "tareas_asignadas"

    def get_queryset(self):
        persona_id = self.request.user.persona_id_persona.id_persona
        tareas_asignadas = Tarea.objects.get_tareas_asignadas()
        context = TareaPersona.objects.get_tareas_asignadas_by_persona(persona_id, tareas_asignadas)
        
        return context


class LoginUserView(FormView):
    template_name = "users/login.html"
    form_class = LoginForm
    success_url = reverse_lazy("app_home:home")

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("app_home:home"))
        return super(LoginUserView, self).get(request, *args, **kwargs)

    def form_valid(self, form):
        username=form.cleaned_data['nombre_usuario']
        password=form.cleaned_data['password_usuario']
        
        encrypted_password = md5DigestHex(password)
        usuario = Usuario.objects.usuario_exists(username, encrypted_password)
        if(usuario):
            rol_id = Usuario.objects.get_usuario_rol_id(username, encrypted_password)[0][4]
            is_rol = Rol.objects.is_rol_nombre(rol_id)

        if usuario and is_rol:
            user = authenticate(username=username, password=encrypted_password)
            if user is not None:
                login(self.request, user)
                for item in Rol.objects.get_rol_nombre(rol_id):
                    messages.success(self.request, f"Has iniciado sesión como {str(item[1]).lower()}")
                return super(LoginUserView, self).form_valid(form)
            else:
                messages.warning(self.request, "Las credenciales ingresadas no son válidas")
                return HttpResponseRedirect(reverse("app_users:login"))   
        else:
            messages.warning(self.request, "Las credenciales ingresadas no son válidas")
            return HttpResponseRedirect(reverse("app_users:login"))   


class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, "Has cerrado sesión correctamente")
        return HttpResponseRedirect(
            reverse(
                'app_users:login'
            )
        )
import datetime
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView, View
from django.views.generic.edit import FormView, FormMixin
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Usuario, Rol, Tarea
from .forms import GestionarTareaForm, LoginForm, TerminarTareaForm
from .functions import md5DigestHex


# Create your views here.
class GestionarTareaView(FormView):
    template_name = "users/tareas.html"
    form_class = GestionarTareaForm
    success_url = reverse_lazy("app_users:tareas-list")

    def form_valid(self, form):
        f_inicio = form.cleaned_data['fecha_inicio']
        f_termino = form.cleaned_data['fecha_termino']

        
        f_inicio = datetime.datetime.strptime(str(f_inicio), '%Y-%m-%d').strftime('%d/%m/%Y')
        f_termino = datetime.datetime.strptime(str(f_termino), '%Y-%m-%d').strftime('%d/%m/%Y')

        f_inicio = datetime.datetime.strptime(f_inicio, '%d/%m/%Y')
        f_termino = datetime.datetime.strptime(f_termino, '%d/%m/%Y')

        diff = f_termino.date() - f_inicio.date()
        current = datetime.date.today() 

        diff_current = f_inicio.date() - current

        if diff.days > 0 and diff_current.days >= 0:
            Tarea.objects.create_tarea(
                form.cleaned_data['titulo_tarea'],
                form.cleaned_data['desc_tarea'],
                form.cleaned_data['fecha_inicio'],
                form.cleaned_data['fecha_termino'],
                form.cleaned_data['etiqueta'],
                porc_cumplimiento=0,
                estado_tarea="Activa")
            return super(GestionarTareaView, self).form_valid(form)
        else:
            return HttpResponseRedirect(reverse("app_users:tareas"))


class TareaListView(LoginRequiredMixin, ListView):
    template_name = "users/list_tareas.html"
    paginate_by = 4
    model = Tarea
    context_object_name = "lista_tareas"
    ordering = ["estado_tarea","-id_tarea"]


def tareaTerminar(request):
    if request.method == "POST":
        id_tarea = request.POST.get("tarea_id")
        if id_tarea != None:
            Tarea.objects.update_tarea(id_tarea)
            return HttpResponseRedirect(reverse("app_users:tareas-list"))
        else:
            return HttpResponseRedirect(reverse("app_home:home"))


def actualizarProgreso(request):
    if request.method == "POST":
        tarea  = Tarea.objects.get_fechas()

        if tarea:
            for item in tarea:
                f_inicio = item.fecha_inicio
                f_termino = item.fecha_termino
                tarea_id = item.id_tarea

                f_inicio = datetime.datetime.strptime(str(f_inicio), '%Y-%m-%d').strftime("%d/%m/%Y")
                f_termino = datetime.datetime.strptime(str(f_termino), '%Y-%m-%d').strftime("%d/%m/%Y")

                f_inicio = datetime.datetime.strptime(f_inicio, '%d/%m/%Y')
                f_termino = datetime.datetime.strptime(f_termino, '%d/%m/%Y')

                diff = f_termino.date() - f_inicio.date()
                currentdate=datetime.date.today()
                diff_actual = f_termino.date() - currentdate

                new_porc_cumplimiento = 100-(diff_actual.days * 100) / diff.days
                if diff_actual.days <= 0:
                    Tarea.objects.update_porc_cumplimiento(100, tarea_id)
                    continue
                elif diff_actual.days == diff.days:
                    new_porc_cumplimiento = 100-(diff_actual.days * 100) / diff.days
                if new_porc_cumplimiento < 0:
                    Tarea.objects.update_porc_cumplimiento(0, tarea_id)
                elif new_porc_cumplimiento > 0:
                    Tarea.objects.update_porc_cumplimiento(new_porc_cumplimiento, tarea_id)
                
            return HttpResponseRedirect(reverse("app_users:tareas-list"))
        else:
            return HttpResponseRedirect(reverse("app_home:tareas-list"))
    else:
        return HttpResponseRedirect(reverse("app_users:tareas-list"))


class LoginUserView(FormView):
    template_name = "users/login.html"
    form_class = LoginForm
    success_url = reverse_lazy("app_home:home")

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
                return super(LoginUserView, self).form_valid(form)
            else:
                return HttpResponseRedirect(reverse("app_users:login"))   
        else:
            return HttpResponseRedirect(reverse("app_users:login"))   


class LogoutView(View):
    def get(self, request, *args, **kargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'app_users:login'
            )
        )
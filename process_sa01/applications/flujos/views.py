from django.shortcuts import render
from django.views.generic import ListView, FormView, TemplateView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import HttpResponseRedirect
from applications.users.models import Tarea, TareaPersona, Estado
from .models import *
from .forms import *


# Create your views here.
class CrearFlujoView(LoginRequiredMixin, TemplateView):
    template_name = "flujos/crear_flujo.html"

    def get(self, request, *args, **kwargs):
        rol_nombre = request.user.rol_id_rol.nombre
        if rol_nombre != 'Gerente' and rol_nombre != 'Funcionario':
            messages.warning(request, "No posees los permisos necesarios para ingresar a la url")
            return HttpResponseRedirect(reverse("app_home:home"))
        return super(CrearFlujoView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CrearFlujoView, self).get_context_data(**kwargs)
        context["tipo_flujo"] = TipoFlujo.objects.get_tipos_flujos()
        context["object_list"] = Tarea.objects.get_tareas_activas()
        return context

        
def crearFlujoTarea(request):
    if request.method == "POST":
        contador_tareas = request.POST.get("tareaContador")
        nombre = request.POST.get("nombre_flujo")
        descripcion = request.POST.get("descripcion")
        tipo_flujo_id = request.POST.get("cboxTipoFlujo")
        lista_tareas = []
        for i in range(1, int(contador_tareas)+1):
            lista_tareas.append(int(request.POST.get(f"tarea{i}")))
        
        lista_objetos_tarea = {Tarea(tarea_id): Tarea(tarea_id) for tarea_id in lista_tareas}
        flujo = Flujo.objects.create_flujo_tarea(nombre, descripcion, TipoFlujo(tipo_flujo_id))
        if flujo:
            last_id_flujo = Flujo.objects.get_last_flujo()
            for tarea in lista_objetos_tarea:
                TareaPersona.objects.crearFlujoTareaPersona(tarea, Flujo(last_id_flujo.id_flujo))
            
            oEstadoId = Estado.objects.get_estado_object(9)
            for tarea_id in lista_tareas:
                Tarea.objects.update_tarea_activa_flujoV2(tarea_id, Estado(oEstadoId))

            if int(contador_tareas) == 1:
                messages.success(request, f"Se ha creado el flujo \"{nombre}\", con {contador_tareas} tarea enlazada")
            elif int(contador_tareas) > 1:
                messages.success(request, f"Se ha creado el flujo \"{nombre}\", con {contador_tareas} tareas enlazadas")
            else:
                messages.error(request, "Ocurrió un error inesperado")
        else:
            messages.error(request, "Error al crear el flujo")
        return HttpResponseRedirect(reverse("app_home:home"))
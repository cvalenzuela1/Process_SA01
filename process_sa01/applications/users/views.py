import random
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
        tarea = Tarea.objects.create_tarea(
            form.cleaned_data['titulo_tarea'],
            form.cleaned_data['desc_tarea'],
            form.cleaned_data['fecha_inicio'],
            form.cleaned_data['fecha_termino'],
            form.cleaned_data['etiqueta'],
            porc_cumplimiento=0,
            estado_tarea="Activa"
        )
        self.request.session["tarea"] = tarea.titulo_tarea
        return super(GestionarTareaView, self).form_valid(form)


class TareaListView(LoginRequiredMixin, ListView):
    template_name = "users/list_tareas.html"
    paginate_by = 3
    model = Tarea
    context_object_name = "lista_tareas"
    ordering = ["estado_tarea","-id_tarea"]
    filterset_class = None


def tareaTerminar(request):
    if request.method == "POST":
        id_tarea = request.POST.get("tarea_id")
        if id_tarea != None:
            Tarea.objects.update_tarea(id_tarea)
            return HttpResponseRedirect(reverse("app_users:tareas-list"))
        else:
            return HttpResponseRedirect(reverse("app_home:home"))


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
                return super(LoginUserView, self).form_valid(form)    
        else:
            return super(LoginUserView, self).form_valid(form)


class LogoutView(View):
    def get(self, request, *args, **kargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'app_users:login'
            )
        )
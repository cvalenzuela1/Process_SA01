from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView, View
from django.views.generic.edit import FormView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Usuario, Rol
from .forms import LoginForm
from .functions import md5DigestHex


# Create your views here.

class UsuarioListView(LoginRequiredMixin, ListView):
    model = Usuario
    template_name = "users/user.html"


class LoginUserView(FormView):
    template_name= "users/login.html"
    form_class = LoginForm
    success_url = reverse_lazy("app_users:user")

    def form_valid(self, form):
        username=form.cleaned_data['nombre_usuario']
        password=form.cleaned_data['password_usuario']
        
        encrypted_password = md5DigestHex(password)
        
        rol_id = Usuario.objects.get_usuario_rol_id(username, encrypted_password)[0][4]
        self.request.session["rol_id"] = rol_id

        is_rol = Rol.objects.is_rol_nombre(rol_id)

        usuario = Usuario.objects.usuario_exists(username, encrypted_password)
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
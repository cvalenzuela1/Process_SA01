from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy

from .forms import LoginForm

# Create your views here.
class LoginUserView(FormView):
    template_name= "users/login.html"
    form_class = LoginForm
    success_url = reverse_lazy("app_home:home")

    def form_valid(self, form):
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password']
        )
        login(self.request, user)
        return super(LoginUserView, self).form_valid(form)
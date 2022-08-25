from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.views.generic import TemplateView

# Create your views here.
class UserView(TemplateView):
    template_name = "users/user.html"


class UserRegisterView(FormView):
    template_name = 'users/register.html'
    # form_class = UserRegisterForm
    # success_url = reverse_lazy
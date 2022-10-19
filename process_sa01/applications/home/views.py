from django.shortcuts import render
from django.views.generic import TemplateView
from applications.users.views import CountTareasSolicitadas

# Create your views here.
class HomeView(CountTareasSolicitadas, TemplateView):
    template_name = "home/home.html"
from django.shortcuts import render
from django.views.generic import TemplateView
from applications.users.views import CountTareasSolicitadas, CountTareasAsignadas
from django.template import RequestContext

# Create your views here.
class HomeView(CountTareasAsignadas, CountTareasSolicitadas, TemplateView):
    template_name = "home/home.html"
from django.urls import path
from . import views

app_name = "app_flujos"

urlpatterns = [
    path("flujos-crear", views.CrearFlujoView.as_view(), name="flujos-crear"),
    path("crear-flujo", views.crearFlujoTarea, name="crear-flujo" )
]
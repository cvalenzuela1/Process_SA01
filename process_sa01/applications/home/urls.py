from django.urls import path
from . import views

app_name = "app_home"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
]
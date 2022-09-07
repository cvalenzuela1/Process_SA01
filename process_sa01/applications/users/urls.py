from django.urls import path
from . import views

app_name = "app_users"

urlpatterns = [
    path("login/", views.LoginUserView.as_view(), name="login"),
]
from django.urls import path
from . import views

app_name = "app_users"

urlpatterns = [
    path("login/", views.LoginUserView.as_view(), name="login"),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('tareas/', views.GestionarTareaView.as_view(), name='tareas'),
    path('tareas-list/', views.TareaListView.as_view(), name='tareas-list'),
    path('tareas-list/<int:page>/', views.TareaListView.as_view(), name='tareas-list-page'),
    path('tareas-terminar', views.tareaTerminar, name='tareas-terminar'),
]
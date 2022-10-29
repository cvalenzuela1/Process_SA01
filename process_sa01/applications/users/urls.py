from django.urls import path
from . import views

app_name = "app_users"

urlpatterns = [
    path("login/", views.LoginUserView.as_view(), name="login"),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('tareas/', views.GestionarTareaView.as_view(), name='tareas'),
    path('tareas-list/', views.TareaListView.as_view(), name='tareas-list'),
    path('tareas-list/<int:page>/', views.TareaListView.as_view(), name='tareas-list-page'),
    path('tareas-terminar/', views.tareaTerminar, name='tareas-terminar'),
    path('tareas-actualizar/', views.actualizarProgreso, name='tareas-actualizar'),
    path('tareas-detalle/<pk>/', views.TareaDetailView.as_view(), name='tareas-detalle'),
    path('tareas-update/', views.updateTarea, name='tareas-update'),
    path('tareas-asignar/', views.AsignarResponsableView.as_view(), name='tareas-asignar'),
    path('tareas-list-solicitadas/', views.TareasSolicitadasListView.as_view(), name='tareas-list-solicitadas'),
    path('tareas-solicitadas-aceptar/', views.tareaAceptar, name='tareas-solicitadas-aceptar'),
    path('tareas-solicitadas-rechazar/', views.tareaRechazar, name='tareas-solicitadas-rechazar'),
    path('tareas-alertar-atrasos/', views.alertarAtrasos, name='tareas-alertar-atrasos'),
    path('tareas-list-asignadas/', views.VerTareasAsignadasListView.as_view(), name='tareas-list-asignadas'),
    # TEST
    path('test1/', views.Test1TemplateView.as_view(), name='test1')
]   
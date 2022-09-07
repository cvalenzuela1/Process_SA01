from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Usuario

# Create your views here.
class HomeView(TemplateView):
    template_name = "home/home.html"

# def student_list(request):
#     usuarios = Usuario.objects.all()
#     context = {
#         'usuarios': usuarios
#     }
#     return render(request, 'users/user.html', context)

class HomeListView(ListView):
    model = Usuario
    template_name = "users/user.html"
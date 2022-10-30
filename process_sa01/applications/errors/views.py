from django.shortcuts import render

# Create your views here.
def handler_404(request, exception):
    return render(request, 'errors/404.html', status=404)
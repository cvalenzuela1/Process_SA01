from django.contrib.auth.backends import ModelBackend
from .models import Usuario

class UsuarioBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None):
        """
        Overrides the authenticate method to allow users to log in using their email address.
        """
        try:
            user = Usuario.objects.get(nombre_usuario=username)
            if Usuario.objects.filter(nombre_usuario=username, password_usuario=password).exists():
                return user
            return None
        except Usuario.DoesNotExist:
            return None

    def get_user(self, user_id):
        """
        Overrides the get_user method to allow users to log in using their email address.
        """
        try:
            return Usuario.objects.get(pk=user_id)
        except Usuario.DoesNotExist:
            return None
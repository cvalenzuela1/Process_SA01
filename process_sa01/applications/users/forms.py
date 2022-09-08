from pyexpat import model
from django import forms
from django.contrib.auth import authenticate
from .models import Usuario

# TODO forms home
class LoginForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = [
            'nombre_usuario',
            'password_usuario'
        ]
        widgets = {
            'nombre_usuario': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': ' Nombre de usuario',
            }),
            'password_usuario': forms.PasswordInput(attrs={
                'placeholder': ' Contraseña',
                'class': 'form-control',
            })
        }
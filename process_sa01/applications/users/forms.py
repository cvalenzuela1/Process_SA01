from django import forms
from .models import Tarea, Usuario

# TODO forms home
class DateInput(forms.DateInput):
    input_type = 'date'


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
                'id': 'password_usuario',
                'placeholder': ' Contraseña',
                'class': 'form-control',
            })
        }

class GestionarTareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = [
            'titulo_tarea',
            'desc_tarea',
            'fecha_inicio',
            'fecha_termino',
            'etiqueta',
        ]
        widgets = {
            'titulo_tarea': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': ' Título de tarea',
                'maxlength': '35'
            }),
            'desc_tarea': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': ' Descripción tarea',
                'rows':3,
                'maxlength': '500'
            }),
            'fecha_inicio': DateInput(attrs={
                'class': 'form-control'
            }),
            'fecha_termino': DateInput(attrs={
                'class': 'form-control'
            }),
            'etiqueta': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': ' Etiqueta',
            })
        }
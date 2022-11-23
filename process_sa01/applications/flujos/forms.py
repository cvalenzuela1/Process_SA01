from django import forms
from .models import *

# class DateInput(forms.DateInput):
#     input_type = 'date'

# class CrearFlujoForm(forms.ModelForm):
#     class Meta:
#         model = Flujo
#         fields = [
#             'nombre_flujo',
#             'descripcion'
#         ]
#         widgets = {
#             'nombre_flujo': forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Nombre de flujo',
#                 'maxlength': '45'
#             }),
#             'descripcion': forms.Textarea(attrs={
#                 'class': 'form-control',
#                 'maxlength': '200',
#                 'placeholder': 'Descripción de flujo',
#                 'cols': '5',
#                 'rows': '2',
#                 'style': 'resize: none'
#             })
#         }
from django.db import models

# Create your models here.

class Usuario(models.Model):
    id_usuario = models.BigAutoField(primary_key=True)
    nombre_usuario = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'usuario'
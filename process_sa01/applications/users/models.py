from django.db import models

# Create your models here.
class Region(models.Model):
    id_region = models.BigAutoField(primary_key=True)
    nombre_region = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'region'


class Ciudad(models.Model):
    id_ciudad = models.BigAutoField(primary_key=True)
    nombre_ciudad = models.CharField(max_length=250)
    region_id_region = models.ForeignKey(Region, on_delete=models.CASCADE, db_column='region_id_region')

    class Meta:
        managed = False
        db_table = 'ciudad'


class Comuna(models.Model):
    id_comuna = models.BigAutoField(primary_key=True)
    nombre_comuna = models.CharField(max_length=100)
    ciudad_id_ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE, db_column='ciudad_id_ciudad')

    class Meta:
        managed = False
        db_table = 'comuna'


class Direccion(models.Model):
    id_direccion = models.BigAutoField(primary_key=True)
    nombre_calle = models.CharField(max_length=250)
    numero_casa = models.BigIntegerField()
    comuna_id_comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE, db_column='comuna_id_comuna')

    class Meta:
        managed = False
        db_table = 'direccion'


class Persona(models.Model):
    id_persona = models.BigAutoField(primary_key=True)
    rut_persona = models.CharField(max_length=10)
    nombre_persona = models.CharField(max_length=30)
    apellido_paterno_persona = models.CharField(max_length=30)
    apellido_materno_persona = models.CharField(max_length=30)
    direccion_id_direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE, db_column='direccion_id_direccion')

    class Meta:
        managed = False
        db_table = 'persona'
        

class Rol(models.Model):
    id_rol = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'rol'


class Usuario(models.Model):
    id_usuario = models.BigAutoField(primary_key=True)
    nombre_usuario = models.CharField(max_length=50, unique=True)
    password_usuario = models.CharField(max_length=50)
    rol_id_rol = models.ForeignKey(Rol, on_delete=models.CASCADE, db_column='rol_id_rol')
    persona_id_persona = models.ForeignKey(Persona, on_delete=models.CASCADE, db_column='persona_id_persona')

    class Meta:
        managed = False
        db_table = 'usuario'



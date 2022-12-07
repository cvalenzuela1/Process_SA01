from django.db import models
from .managers import *

# Create your models here.
class TipoFlujo(models.Model):
    id_tipo_flujo = models.BigAutoField(primary_key=True)
    tipo = models.CharField(max_length=200)

    objects = TipoFlujoManager()

    class Meta:
        managed = False
        db_table = 'tipo_flujo'


class EstadoFlujo(models.Model):
    id_estado_flujo = models.BigAutoField(primary_key=True)
    estado_flujo = models.CharField(max_length=50)

    objects = EstadoFlujoManager()

    class Meta:
        managed = False
        db_table = 'estado_flujo'


class Flujo(models.Model):
    id_flujo = models.BigAutoField(primary_key=True)
    nombre_flujo = models.CharField(max_length=100)
    fecha_creacion = models.DateField()
    fecha_primera_ejecucion = models.DateField(blank=True, null=True)
    fecha_ultima_ejecucion = models.DateField(blank=True, null=True)
    fecha_proxima_ejecucion = models.DateField(blank=True, null=True)
    descripcion = models.CharField(max_length=200)
    tipo_flujo_id_tipo_flujo = models.ForeignKey('TipoFlujo', models.CASCADE, db_column='tipo_flujo_id_tipo_flujo')
    estado_flujo_flujo = models.ForeignKey(EstadoFlujo, models.CASCADE, db_column='estado_flujo_flujo')

    objects = FlujoTareaManager()

    class Meta:
        managed = False
        db_table = 'flujo'
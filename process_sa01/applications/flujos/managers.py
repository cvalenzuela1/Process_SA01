from django.db import models
from django.db.models import Q
from .functions import *

class FlujoTareaManager(models.Manager):
    def create_flujo_tarea(self, nombre_flujo, descripcion, tipo_flujo):
        flujo = self.model(
            nombre_flujo=nombre_flujo,
            descripcion=descripcion,
            fecha_creacion=getCurrentDate(),
            tipo_flujo_id_tipo_flujo=tipo_flujo
        )
        flujo.save(using=self.db)
        return flujo

    def get_last_flujo(self):
        return self.all().order_by("-id_flujo").first()

    def get_count_anual(self):
        return self.all().filter(
            tipo_flujo_id_tipo_flujo=1
        ).count()

    def get_count_mensual(self):
        return self.all().filter(
            tipo_flujo_id_tipo_flujo=2
        ).count()

    def get_count_semanal(self):
        return self.all().filter(
            tipo_flujo_id_tipo_flujo=3
        ).count()

    def get_count_diario(self):
        return self.all().filter(
            tipo_flujo_id_tipo_flujo=4
        ).count()

class TipoFlujoManager(models.Manager):
    def get_tipos_flujos(self):
        return self.all()
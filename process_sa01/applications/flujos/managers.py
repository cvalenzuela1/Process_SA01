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

class TipoFlujoManager(models.Manager):
    def get_tipos_flujos(self):
        return self.all()

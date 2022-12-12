from django.db import models
from django.db.models import Q
from .functions import *

class FlujoTareaManager(models.Manager):
    def create_flujo_tarea(self, nombre_flujo, descripcion, tipo_flujo, estado_flujo):
        flujo = self.model(
            nombre_flujo=nombre_flujo,
            descripcion=descripcion,
            fecha_creacion=getCurrentDate(),
            tipo_flujo_id_tipo_flujo=tipo_flujo,
            estado_flujo_flujo=estado_flujo
            # fecha_proxima_ejecucion=proxima_ejecucion
        )
        flujo.save(using=self.db)
        return flujo

    def get_last_flujo(self):
        return self.all().order_by("-id_flujo").first()

    def actualizar_estado_flujo(self, flujo_id, proxima_ejecucion):
        if self.filter(id_flujo=flujo_id).filter(fecha_primera_ejecucion__isnull=True):
            self.filter(
                id_flujo=flujo_id
            ).update(
                estado_flujo_flujo=2,
                fecha_primera_ejecucion=getCurrentDate(),
                fecha_ultima_ejecucion=getCurrentDate(),
                fecha_proxima_ejecucion=proxima_ejecucion
            )
            return 1
        elif self.filter(id_flujo=flujo_id).filter(fecha_primera_ejecucion__isnull=False):
            if self.filter(id_flujo=flujo_id).filter(fecha_proxima_ejecucion=getCurrentDate()):
                self.filter(
                    id_flujo=flujo_id
                ).update(
                    estado_flujo_flujo=2,
                    fecha_ultima_ejecucion=getCurrentDate(),
                    fecha_proxima_ejecucion=proxima_ejecucion
                )
                return 2
            else:
                return 3
        else:
            return 0

    def finalizar_flujos(self):
        return self.all().filter(
            fecha_proxima_ejecucion=getCurrentDate()
        ).update(
            estado_flujo_flujo=3
        )

    # GRAFICOS
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

class EstadoFlujoManager(models.Manager):
    def get_estadoflujo_activo(self):
        return self.all().filter(
            id_estado_flujo=1
        )
from django.db import models
from django.db.models import Q

class UsuarioManager(models.Manager):
    
    def get_usuario_rol_id(self, username, password):
        return self.filter(
            nombre_usuario=username,
            password_usuario=password
        ).values_list()

    def usuario_exists(self, username, password):
        return self.filter(
            nombre_usuario=username,
            password_usuario=password
        ).exists()


class RolManager(models.Manager):
    
    def is_rol_nombre(self, rol_id):
        return self.all().filter(
            Q(nombre="Funcionario") | Q(nombre="Diseñador de procesos") 
        ).filter(
            id_rol=rol_id
        ).exists()


class TareaManager(models.Manager):

    def create_tarea(self, titulo, descripcion, fecha_inicio, fecha_termino, etiqueta, **extra_fields):
        tarea = self.model(
            titulo_tarea=titulo,
            desc_tarea=descripcion,
            fecha_inicio=fecha_inicio,
            fecha_termino=fecha_termino,
            etiqueta=etiqueta,
            **extra_fields
        )
        tarea.save(using=self.db)
        return tarea

    def update_tarea(self, tarea_id):
        self.filter(
            id_tarea=tarea_id
        ).update(
            estado_tarea="Finalizada",
            porc_cumplimiento=100
        )

    def update_porc_cumplimiento(self, porc_actualizado, tarea_id):
        
        if porc_actualizado >= 100:
            self.filter(
                id_tarea=tarea_id
            ).update(
                estado_tarea="Finalizada",
                porc_cumplimiento=100
            )
        else:
            self.filter(
                id_tarea=tarea_id
            ).update(
                porc_cumplimiento=porc_actualizado
            )
        

    def get_fechas(self):
        items = self.all()
        return items

    def all_tareas(self):
        return self.all()
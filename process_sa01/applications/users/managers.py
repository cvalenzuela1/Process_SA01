from operator import mod
from django.db import models
from django.db.models import Q

from .functions import getCurrentDate


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
            Q(nombre="Funcionario") | Q(nombre="Diseñador de procesos") | Q(nombre="Gerente")
        ).filter(
            id_rol=rol_id
        ).exists()

    def get_rol_nombre(self, rol_id):
        return self.filter(
            id_rol=rol_id
        ).values_list()


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

    def update_tarea(self, tarea_id, current):
        self.filter(
            id_tarea=tarea_id
        ).update(
            estado_id_estado=4,
            estado_alterado=1,
            fecha_estado_alterado=current,
            porc_cumplimiento=100
        )

    def update_tarea_estado(self, lista_tareas):

        for tarea in lista_tareas:
            self.filter(
                id_tarea=tarea
            ).update(
                estado_id_estado=2
            )

    def update_porc_cumplimiento(self, porc_actualizado, tarea_id):
        
        if porc_actualizado >= 100:
            self.filter(
                id_tarea=tarea_id
            ).update(
                estado_id_estado=4,
                porc_cumplimiento=100,
                estado_alterado=1,
                fecha_estado_alterado=getCurrentDate()
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

    def get_fecha_termino(self, pk):
        return self.filter(
            id_tarea=pk
        ).values_list()[0][4]

    def update_tarea_fields(self, tarea_id, titulo, desc, etiqueta, ftermino):

        if titulo != None and len(titulo) > 0:
            self.filter(
                id_tarea=tarea_id
            ).update(
                titulo_tarea=titulo
            )
        if desc != None and len(desc) > 0:
            self.filter(
                id_tarea=tarea_id
            ).update(
                desc_tarea=desc
            )
        if etiqueta != None and len(etiqueta) > 0:
            self.filter(
                id_tarea=tarea_id
            ).update(
                etiqueta=etiqueta
            )
        if ftermino != None and len(ftermino) > 0:
            self.filter(
                id_tarea=tarea_id
            ).update(
                fecha_termino=ftermino
            )
        
    def get_tareas_new_order(self, rol_nombre):
        
        if rol_nombre == "Funcionario" or rol_nombre == "Diseñador de procesos":
            return self.all().filter(
                Q(estado_alterado=0) | Q(estado_alterado=1)
            ).order_by(
                'estado_alterado',
                '-id_tarea'
            )
        elif rol_nombre == "Gerente":
            return self.all().filter(
                Q(estado_alterado=0) | Q(estado_alterado=1) | Q(estado_alterado=2)
            ).order_by(
                'estado_alterado',
                '-id_tarea'
            )

    def get_tareas_new_order1(self):
        
        return self.all().filter(
            Q(estado_alterado=0) | Q(estado_alterado=1)
        ).order_by(
            'estado_alterado',
            '-id_tarea'
        )
    
    def get_tareas_new_order2(self):
        
        return self.all().filter(
            estado_alterado=0
        ).order_by(
            'id_tarea'
        )

class PersonaManager(models.Manager):

    def get_persona(self):
        return self.all()


class TareaPersonaManager(models.Manager):

    def create_tarea_persona(self, persona_id, lista_tareas):

        for tarea in lista_tareas:
            tarea_persona = self.model(
                persona_id_persona= persona_id,
                tarea_id_tarea= lista_tareas[tarea],
            )
            tarea_persona.save(using=self.db)

    def get_tarea_by_id(self, tarea_id):
        return self.filter(
            tarea_id_tarea=tarea_id
            )


class EstadoManager(models.Manager):
    
    def get_estado(self, estado_nombre):
        return self.filter(
            estado=estado_nombre
        ).values_list()

    def get_estado_nombre(self, estado_id):
        return self.filter(
            id_estado=estado_id
        ).values_list()
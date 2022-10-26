from email.charset import QP
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

    def get_funcionarios_cliente(self):
        return self.all().filter(
            rol_id_rol=3
        )

class RolManager(models.Manager):
    
    def is_rol_nombre(self, rol_id):
        return self.all().filter(
            Q(nombre="Funcionario") | Q(nombre="Diseñador de procesos") | Q(nombre="Gerente") | Q(nombre="Funcionario Cliente")
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
                estado_id_estado=5
            )

    def update_porc_cumplimiento(self, porc_actualizado, tarea_id):
        
        if porc_actualizado >= 100:
            self.filter(
                id_tarea=tarea_id
            ).update(
                estado_id_estado=7,
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
        
    def get_tareas_new_order(self, rol_id):
        if rol_id == 2:
            return self.all().filter(
                Q(estado_alterado=0) | Q(estado_alterado=1)
            ).filter(
               ~Q(estado_id_estado=5) 
            ).order_by(
                'estado_alterado',
                '-id_tarea'
            )
        elif rol_id == 4:
            return self.all().filter(
                Q(estado_alterado=0) | Q(estado_alterado=1) | Q(estado_alterado=2)
            ).filter(
               ~Q(estado_id_estado=5) 
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

    def get_tareas_solicitadas(self):
        return self.all().filter(
            estado_id_estado=5
        )

    def update_tarea_solicitada(self, tarea_id):
        self.filter(
            id_tarea=tarea_id
        ).update(
            estado_id_estado=2
        )

    def update_tarea_rechazada(self, tarea_id):
        self.filter(
            id_tarea=tarea_id
        ).update(
            estado_id_estado=6
        )

    def get_tareas_asignadas_atrasadas_ejecucion(self):
        return self.all().filter(
            Q(estado_id_estado=2) | Q(estado_id_estado=3) | Q(estado_id_estado=7)
        )

    def get_tareas_atrasadas(self):
        return self.all().filter(
            estado_id_estado=7
        )

    def update_tarea_diferencia_dias_fechas(self, tarea_id, diferencia_dias):
        return self.filter(
            id_tarea=tarea_id
        ).update(
            diferencia_dias_fechas=diferencia_dias
        )


class PersonaManager(models.Manager):

    def get_persona(self):
        return self.all()

    def get_persona_funcionario_cliente(self, funcionarios_cliente):

        lista = []
        for funcionario in funcionarios_cliente:
            if self.all().filter(
                id_persona=funcionario.persona_id_persona.id_persona
            ).exists():
                lista.append(self.all().filter(
                    id_persona=funcionario.persona_id_persona.id_persona
                ))
        return lista

    def get_persona_by_id(self, persona_id):
        return self.filter(
            id_persona=persona_id
        )


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

    def get_tareas_solicitadas_by_persona(self, persona_id, tareas_solicitadas):
        lista = []
        len1 = len(tareas_solicitadas)
        for tarea in tareas_solicitadas:
            if self.filter(
                persona_id_persona=persona_id,
                tarea_id_tarea=tarea.id_tarea
            ).exists():
                lista.append(self.filter(
                persona_id_persona=persona_id,
                tarea_id_tarea=tarea.id_tarea
            ))
        return lista

    def get_tareas_asignadas_by_persona(self, persona_id, tareas_asignadas):
        lista = []
        for tarea in tareas_asignadas:
            if self.filter(
                persona_id_persona=persona_id,
                tarea_id_tarea=tarea.id_tarea
            ).exists():
                lista.append(self.filter(
                persona_id_persona=persona_id,
                tarea_id_tarea=tarea.id_tarea
            ))
        return lista
    
    def count_tareas_solicitadas_by_persona(self, persona_id, tareas_solicitadas):
        lista = []
        for tarea in tareas_solicitadas:
            if self.filter(
                persona_id_persona=persona_id,
                tarea_id_tarea=tarea.id_tarea
            ).exists():
                lista.append(self.filter(
                persona_id_persona=persona_id,
                tarea_id_tarea=tarea.id_tarea
            ))
        return len(lista)

    def count_tareas_asignadas_by_persona(self, persona_id, tareas_asignadas):
        lista = []
        for tarea in tareas_asignadas:
            if self.filter(
                persona_id_persona=persona_id,
                tarea_id_tarea=tarea.id_tarea
            ).exists():
                lista.append(self.filter(
                persona_id_persona=persona_id,
                tarea_id_tarea=tarea.id_tarea
            ))
        return len(lista)

    def get_tareas_by_tareas_atrasadas(self, tareas_atrasadas):
        lista = []
        for tarea in tareas_atrasadas:
            if self.filter(
                tarea_id_tarea=tarea.id_tarea
            ).exists():
                lista.append(self.filter(
                    tarea_id_tarea=tarea.id_tarea
                ))
        return lista

    def update_justificacion_rechazo(self, tarea_id, justificacion):
        self.filter(
            tarea_id_tarea=tarea_id
        ).update(
            justificacion_rechazo=justificacion
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
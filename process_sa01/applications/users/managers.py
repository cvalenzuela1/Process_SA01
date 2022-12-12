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

    # DATOS GRÁFICO TABLERO GLOBAL
    def get_count_gerente(self):
        return self.all().filter(
            rol_id_rol=4
        ).count()

    def get_count_funcionario(self):
        return self.all().filter(
            rol_id_rol=2
        ).count()

    def get_count_cliente(self):
        return self.all().filter(
            rol_id_rol=3
        ).count()

    def get_count_disenador(self):
        return self.all().filter(
            rol_id_rol=5
        ).count()


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

    def update_tarea_reasignar(self, tarea_id, fecha_inicio, fecha_termino_nueva):
        self.filter(
            id_tarea=tarea_id
        ).update(
            fecha_inicio=fecha_inicio,
            porc_cumplimiento=0,
            fecha_termino=fecha_termino_nueva
        )

    def update_tarea(self, tarea_id):
        self.filter(
            id_tarea=tarea_id
        ).update(
            estado_id_estado=4,
            porc_cumplimiento=100
        )

    def update_tarea_estado(self, lista_tareas):
        for tarea in lista_tareas:
            self.filter(
                id_tarea=tarea
            ).update(
                estado_id_estado=5
            )

    def update_tarea_estado_reasignar(self, tarea_id):
        self.filter(
            id_tarea=tarea_id
        ).update(
            estado_id_estado=2
        )

    def update_porc_cumplimiento(self, porc_actualizado, tarea_id):
        if porc_actualizado >= 100:
            self.filter(
                id_tarea=tarea_id
            ).update(
                estado_id_estado=7,
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

    def get_tareas_activas(self):
        return self.all().filter(
            estado_id_estado = 1
        )

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
        if rol_id == 2: #Rol funcionario
            return self.all().filter(
                Q(estado_id_estado=1) | Q(estado_id_estado=2) | Q(estado_id_estado=3) | Q(estado_id_estado=7)
            ).order_by(
                'estado_id_estado',
                '-id_tarea'
            )
        elif rol_id == 4: #Rol gerente
            return self.all().filter(
                Q(estado_id_estado=1) | Q(estado_id_estado=2) | Q(estado_id_estado=3) | Q(estado_id_estado=4) | Q(estado_id_estado=5) | Q(estado_id_estado=6) | Q(estado_id_estado=7) | Q(estado_id_estado=8)
            ).order_by(
                'estado_id_estado',
                '-id_tarea'
            )
    
    def get_tareas_new_order2(self):
        return self.all().filter(
            Q(estado_id_estado=1) | Q(estado_id_estado=9)
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

    def count_tareas(self, rol_id):
        if rol_id == 2: #Rol funcionario
            return self.all().filter(
                Q(estado_id_estado=1) | Q(estado_id_estado=2) | Q(estado_id_estado=3) | Q(estado_id_estado=7)
            ).count()
        elif rol_id == 4: #Rol gerente
            return self.all().filter(
                Q(estado_id_estado=1) | Q(estado_id_estado=2) | Q(estado_id_estado=3) | Q(estado_id_estado=4) | Q(estado_id_estado=5) | Q(estado_id_estado=6) | Q(estado_id_estado=7) | Q(estado_id_estado=8)
            ).count()

    def update_tarea_activa_flujo(self, tarea_id):
        self.filter(
            id_tarea=tarea_id
        ).update(
            estado_id_estado=9
        )

    def update_tarea_activa_flujoV2(self, tarea_id, estado_id):
        oTarea = self.get(
            id_tarea=tarea_id
        )
        oTarea.estado_id_estado = estado_id
        oTarea.save()

    def get_tareas_reasignar(self):
        return self.all().filter(
            Q(estado_id_estado=4) | Q(estado_id_estado=6) | Q(estado_id_estado=8)
        ).order_by(
            'id_tarea'
        )
    
    # DATOS GRAFICOS
    def get_count_activas(self):
        return self.all().filter(
            estado_id_estado=1
        ).count()
    
    def get_count_asignadas(self):
        return self.all().filter(
            estado_id_estado=2
        ).count()

    def get_count_ejecucion(self):
        return self.all().filter(
            estado_id_estado=3
        ).count()

    def get_count_finalizadas(self):
        return self.all().filter(
            estado_id_estado=4
        ).count()

    def get_count_solicitadas(self):
        return self.all().filter(
            estado_id_estado=5
        ).count()

    def get_count_rechazadas(self):
        return self.all().filter(
            estado_id_estado=6
        ).count()

    def get_count_atrasadas(self):
        return self.all().filter(
            estado_id_estado=7
        ).count()

    def get_count_vencidas(self):
        return self.all().filter(
            estado_id_estado=8
        ).count()

    def get_count_activasflujo(self):
        return self.all().filter(
            estado_id_estado=9
        ).count()

    #CONTAR FECHAS INICIO - TERMINO ESTE MES
    def get_count_finicio(self):
        return self.all().filter(
            estado_id_estado=4
        ).count()

    def get_count_ftermino(self):
        return self.all().filter(
            estado_id_estado=7
        ).count()


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

    def create_tarea_persona(self, persona_id, lista_tareas, responsable_id, current_date):
        for tarea in lista_tareas:
            tarea_persona = self.model(
                persona_id_persona=persona_id,
                tarea_id_tarea=lista_tareas[tarea],
                responsable_id_responsable=responsable_id,
                fecha_asignacion_tarea=current_date
            )
            tarea_persona.save(using=self.db)

    def update_tarea_persona_reasignar(self, tarea_id, persona_id, responsable_id):
        self.filter(
            tarea_id_tarea=tarea_id
        ).update(
            responsable_id_responsable=responsable_id,
            persona_id_persona=persona_id
        )

    def get_tarea_by_id(self, tarea_id):
        return self.filter(
            tarea_id_tarea=tarea_id
        )

    def get_tareas_solicitadas_by_persona(self, persona_id, tareas_solicitadas):
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

    def get_personas_responsable(self, persona_id):
        return self.filter(
            responsable_id_responsable=persona_id
        ).order_by("-tarea_id_tarea")
    
    def count_personas_responsable(self, persona_id):
        return self.filter(
            responsable_id_responsable=persona_id
        ).count()

    def asignarFlujo(self, tareas, flujo_id):
        for tarea in tareas:
            self.filter(
                tarea_id_tarea=tarea
            ).update(
                flujo_id_flujo=flujo_id
            )

    def crearFlujoTareaPersona(self, tarea_id, flujo_id):
            tarea_persona = self.model(
                flujo_id_flujo=flujo_id,
                tarea_id_tarea=tarea_id
            )
            tarea_persona.save(using=self.db)

    def get_flujo_tarea_notnull(self):
        return self.exclude(
            flujo_id_flujo__isnull = True
        ).order_by('-flujo_id_flujo')

    # DATOS GRAFICOS
    def get_count_asignadasPersona(self, responsable_id):
        return self.all().filter(
            tarea_id_tarea__estado_id_estado__id_estado=2,
            responsable_id_responsable=responsable_id
        ).count()

    def get_count_ejecucionPersona(self, responsable_id):
        return self.all().filter(
            tarea_id_tarea__estado_id_estado__id_estado=3,
            responsable_id_responsable=responsable_id
        ).count()

    def get_count_finalizadasPersona(self, responsable_id):
        return self.all().filter(
            tarea_id_tarea__estado_id_estado__id_estado=4,
            responsable_id_responsable=responsable_id
        ).count()

    def get_count_atrasadasPersona(self, responsable_id):
        return self.all().filter(
            tarea_id_tarea__estado_id_estado__id_estado=7,
            responsable_id_responsable=responsable_id
        ).count()

    def get_tareas_persona_id(self, persona_id):
        return self.filter(
            persona_id_persona=persona_id,
        ).filter(
            Q(tarea_id_tarea__estado_id_estado__id_estado=2) | Q(tarea_id_tarea__estado_id_estado__id_estado=5)
        ).order_by("-tarea_id_tarea")

    def get_persona_byidPersonaTarea(self, persona_id, tarea_id):
        return self.filter(
            persona_id_persona=persona_id,
            tarea_id_tarea=tarea_id
        ).order_by("-tarea_id_tarea")


class EstadoManager(models.Manager):
    
    def get_estado(self, estado_nombre):
        return self.filter(
            estado=estado_nombre
        ).values_list()

    def get_estado_nombre(self, estado_id):
        return self.filter(
            id_estado=estado_id
        ).values_list()

    def get_estado_object(self, estado_id):
        return self.filter(
            id_estado=estado_id
        ).values_list()[0][0]

class DepartamentoManager(models.Manager):
    def get_count_all(self):
        return self.all()


class ReportarProblemaManager(models.Manager):
    def create_reporte_problema(self, tarea_id, descripcion_problema, persona_id, current_date):
        reporte_problema = self.model(
            descripcion_reporte=descripcion_problema,
            fecha_generacion=current_date,
            persona_id_persona=persona_id,
            tarea_id_tarea=tarea_id
        )
        reporte_problema.save(using=self.db)
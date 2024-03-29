from django.db import models
from .managers import * 
from applications.flujos.models import Flujo

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


class Estado(models.Model):
    id_estado = models.BigAutoField(primary_key=True)
    estado = models.CharField(max_length=50)

    objects = EstadoManager()

    class Meta:
        managed = False
        db_table = 'estado'


class Tarea(models.Model):
    id_tarea = models.BigAutoField(primary_key=True)
    titulo_tarea = models.CharField(max_length=50)
    desc_tarea = models.CharField(max_length=500)
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField()
    etiqueta = models.CharField(max_length=50)
    porc_cumplimiento = models.BigIntegerField()
    diferencia_dias_fechas = models.BigIntegerField()
    estado_id_estado = models.ForeignKey(Estado, on_delete=models.CASCADE, db_column='estado_id_estado')

    objects = TareaManager()

    def __unicode__(self):
        return self.id_tarea

    class Meta:
        managed = False
        db_table = 'tarea'


class Subgerencia(models.Model):
    id_subgerencia = models.BigAutoField(primary_key=True)
    subgerencia = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'subgerencia'


class Departamento(models.Model):
    id_departamento = models.BigAutoField(primary_key=True)
    departamento = models.CharField(max_length=150)

    objects = DepartamentoManager()

    class Meta:
        managed = False
        db_table = 'departamento'


class Gerencia(models.Model):
    id_gerencia = models.BigAutoField(primary_key=True)
    gerencia = models.CharField(max_length=150)
    departamento_id_departamento = models.ForeignKey(Departamento, models.CASCADE, db_column='departamento_id_departamento', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gerencia'


class Persona(models.Model):
    id_persona = models.BigAutoField(primary_key=True)
    rut_persona = models.CharField(max_length=10)
    nombre_persona = models.CharField(max_length=30)
    apellido_paterno_persona = models.CharField(max_length=30)
    apellido_materno_persona = models.CharField(max_length=30)
    email_persona = models.CharField(max_length=50)
    direccion_id_direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE, db_column='direccion_id_direccion')
    departamento_id_departamento = models.ForeignKey(Departamento, models.CASCADE, db_column='departamento_id_departamento')

    objects = PersonaManager()

    def __unicode__(self):
        return self.id_persona

    class Meta:
        managed = False
        db_table = 'persona'


class ReportarProblema(models.Model):
    id_reporte = models.BigAutoField(primary_key=True)
    descripcion_reporte = models.CharField(max_length=250)
    fecha_generacion = models.DateField()
    persona_id_persona = models.ForeignKey(Persona, models.DO_NOTHING, db_column='persona_id_persona')
    tarea_id_tarea = models.ForeignKey('Tarea', models.DO_NOTHING, db_column='tarea_id_tarea')

    objects = ReportarProblemaManager()

    class Meta:
        managed = False
        db_table = 'reportar_problema'


class Responsable(models.Model):
    persona_id_persona = models.OneToOneField(Persona, models.CASCADE, db_column='persona_id_persona', primary_key=True)
    fecha_generacion = models.DateField()

    class Meta:
        managed = False
        db_table = 'responsable'


class TareaPersona(models.Model):
    id_tarea_persona = models.BigAutoField(primary_key=True)
    persona_id_persona = models.ForeignKey(Persona, models.CASCADE, db_column='persona_id_persona', blank=True, null=True)
    tarea_id_tarea = models.ForeignKey(Tarea, models.CASCADE, db_column='tarea_id_tarea')
    justificacion_rechazo = models.CharField(max_length=300, blank=True, null=True)
    responsable_id_responsable = models.ForeignKey(Responsable, models.CASCADE, db_column='responsable_id_responsable', blank=True, null=True)
    fecha_asignacion_tarea = models.DateField(blank=True, null=True)
    flujo_id_flujo = models.ForeignKey(Flujo, models.CASCADE, db_column='flujo_id_flujo', blank=True, null=True)

    objects = TareaPersonaManager()

    class Meta:
        managed = False
        db_table = 'tarea_persona'


class Rol(models.Model):
    id_rol = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    objects = RolManager()

    class Meta:
        managed = False
        db_table = 'rol'


class Usuario(models.Model):
    id_usuario = models.BigAutoField(primary_key=True)
    nombre_usuario = models.CharField(max_length=50)
    password_usuario = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    rol_id_rol = models.ForeignKey(Rol, on_delete=models.CASCADE, related_name="rol_usuario", db_column='rol_id_rol')
    persona_id_persona = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name="persona_usuario", db_column='persona_id_persona')
    is_authenticated = True

    objects = UsuarioManager()
    
    class Meta:
        managed = False
        db_table = 'usuario'
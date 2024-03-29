# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Ciudad(models.Model):
    id_ciudad = models.BigAutoField(primary_key=True)
    nombre_ciudad = models.CharField(max_length=250)
    region_id_region = models.ForeignKey('Region', models.DO_NOTHING, db_column='region_id_region')

    class Meta:
        managed = False
        db_table = 'ciudad'


class Comuna(models.Model):
    id_comuna = models.BigAutoField(primary_key=True)
    nombre_comuna = models.CharField(max_length=100)
    ciudad_id_ciudad = models.ForeignKey(Ciudad, models.DO_NOTHING, db_column='ciudad_id_ciudad')

    class Meta:
        managed = False
        db_table = 'comuna'


class Departamento(models.Model):
    id_departamento = models.BigAutoField(primary_key=True)
    departamento = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'departamento'


class Direccion(models.Model):
    id_direccion = models.BigAutoField(primary_key=True)
    nombre_calle = models.CharField(max_length=250)
    numero_casa = models.BigIntegerField()
    comuna_id_comuna = models.ForeignKey(Comuna, models.DO_NOTHING, db_column='comuna_id_comuna')

    class Meta:
        managed = False
        db_table = 'direccion'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200, blank=True, null=True)
    action_flag = models.IntegerField()
    change_message = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField(blank=True, null=True)
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Estado(models.Model):
    id_estado = models.BigAutoField(primary_key=True)
    estado = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'estado'


class EstadoFlujo(models.Model):
    id_estado_flujo = models.BigAutoField(primary_key=True)
    estado_flujo = models.CharField(max_length=50)

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
    tipo_flujo_id_tipo_flujo = models.ForeignKey('TipoFlujo', models.DO_NOTHING, db_column='tipo_flujo_id_tipo_flujo')
    estado_flujo_flujo = models.ForeignKey(EstadoFlujo, models.DO_NOTHING, db_column='estado_flujo_flujo')

    class Meta:
        managed = False
        db_table = 'flujo'


class Gerencia(models.Model):
    id_gerencia = models.BigAutoField(primary_key=True)
    gerencia = models.CharField(max_length=150)
    departamento_id_departamento = models.ForeignKey(Departamento, models.DO_NOTHING, db_column='departamento_id_departamento', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gerencia'


class Persona(models.Model):
    id_persona = models.BigAutoField(primary_key=True)
    rut_persona = models.CharField(unique=True, max_length=10)
    nombre_persona = models.CharField(max_length=30)
    apellido_paterno_persona = models.CharField(max_length=30)
    apellido_materno_persona = models.CharField(max_length=30)
    email_persona = models.CharField(max_length=50)
    direccion_id_direccion = models.ForeignKey(Direccion, models.DO_NOTHING, db_column='direccion_id_direccion')
    departamento_id_departamento = models.ForeignKey(Departamento, models.DO_NOTHING, db_column='departamento_id_departamento', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'persona'


class Region(models.Model):
    id_region = models.BigAutoField(primary_key=True)
    nombre_region = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'region'


class ReportarProblema(models.Model):
    id_reporte = models.BigAutoField(primary_key=True)
    descripcion_reporte = models.CharField(max_length=250)
    fecha_generacion = models.DateField()
    persona_id_persona = models.ForeignKey(Persona, models.DO_NOTHING, db_column='persona_id_persona')
    tarea_id_tarea = models.ForeignKey('Tarea', models.DO_NOTHING, db_column='tarea_id_tarea')

    class Meta:
        managed = False
        db_table = 'reportar_problema'


class Responsable(models.Model):
    persona_id_persona = models.OneToOneField(Persona, models.DO_NOTHING, db_column='persona_id_persona', primary_key=True)
    fecha_generacion = models.DateField()

    class Meta:
        managed = False
        db_table = 'responsable'


class Rol(models.Model):
    id_rol = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'rol'


class Tarea(models.Model):
    id_tarea = models.BigAutoField(primary_key=True)
    titulo_tarea = models.CharField(max_length=50)
    desc_tarea = models.CharField(max_length=500)
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField()
    etiqueta = models.CharField(max_length=50)
    porc_cumplimiento = models.BigIntegerField()
    diferencia_dias_fechas = models.BigIntegerField()
    estado_id_estado = models.ForeignKey(Estado, models.DO_NOTHING, db_column='estado_id_estado')

    class Meta:
        managed = False
        db_table = 'tarea'


class TareaPersona(models.Model):
    id_tarea_persona = models.BigAutoField(primary_key=True)
    persona_id_persona = models.ForeignKey(Persona, models.DO_NOTHING, db_column='persona_id_persona', blank=True, null=True)
    tarea_id_tarea = models.ForeignKey(Tarea, models.DO_NOTHING, db_column='tarea_id_tarea')
    justificacion_rechazo = models.CharField(max_length=300, blank=True, null=True)
    responsable_id_responsable = models.ForeignKey(Responsable, models.DO_NOTHING, db_column='responsable_id_responsable', blank=True, null=True)
    fecha_asignacion_tarea = models.DateField(blank=True, null=True)
    flujo_id_flujo = models.ForeignKey(Flujo, models.DO_NOTHING, db_column='flujo_id_flujo', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tarea_persona'


class TipoFlujo(models.Model):
    id_tipo_flujo = models.BigAutoField(primary_key=True)
    tipo = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'tipo_flujo'


class Usuario(models.Model):
    id_usuario = models.BigAutoField(primary_key=True)
    nombre_usuario = models.CharField(unique=True, max_length=50)
    password_usuario = models.CharField(max_length=50)
    is_active = models.BooleanField()
    rol_id_rol = models.ForeignKey(Rol, models.DO_NOTHING, db_column='rol_id_rol')
    persona_id_persona = models.ForeignKey(Persona, models.DO_NOTHING, db_column='persona_id_persona')

    class Meta:
        managed = False
        db_table = 'usuario'

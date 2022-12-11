import hashlib
import datetime
from django.db import connection

def md5DigestHex(text):
    hex_string = hashlib.md5(text.encode("utf-8")).hexdigest()
    return hex_string

def getCurrentDate():
    current = datetime.date.today()
    return current

def getDiffDaysTerminoInicio(f_termino, f_inicio):
    f_inicio = datetime.datetime.strptime(str(f_inicio), '%Y-%m-%d').strftime("%d/%m/%Y")
    f_termino = datetime.datetime.strptime(str(f_termino), '%Y-%m-%d').strftime("%d/%m/%Y")

    f_inicio = datetime.datetime.strptime(f_inicio, '%d/%m/%Y')
    f_termino = datetime.datetime.strptime(f_termino, '%d/%m/%Y')
    diff = f_termino.date() - f_inicio.date()

    return diff

def getDiffDaysTerminoCurrent(f_termino):
    f_termino = datetime.datetime.strptime(str(f_termino), '%Y-%m-%d').strftime("%d/%m/%Y")
    f_termino = datetime.datetime.strptime(f_termino, '%d/%m/%Y')
    currentdate=datetime.date.today()
    diff_actual = f_termino.date() - currentdate

    return diff_actual

def getDiffDaysCurrentInicio(f_inicio):
    f_inicio = datetime.datetime.strptime(str(f_inicio), '%Y-%m-%d').strftime("%d/%m/%Y")
    f_inicio = datetime.datetime.strptime(f_inicio, '%d/%m/%Y')
    currentdate=datetime.date.today()
    diff_actual_inicio = f_inicio.date() - currentdate

    return diff_actual_inicio

def executeSPUpdateEstadoAlterado():
    cursor = connection.cursor()
    try:
        sentencia = "PD_TRG_UPDATE_ESTADO_ALTERADO"
        cursor.callproc(sentencia)
    except Exception as e:
        print("ERROR: ", e, "\nSentencia: ", sentencia)
    finally:
        cursor.close()

def executeSPUpdateEstadoTareas():
    cursor = connection.cursor()
    try:
        sentencia = "PD_UPDATE_ESTADO_TAREAS"
        cursor.callproc(sentencia)
    except Exception as e:
        print("ERROR: ", e, "\nSentencia: ", sentencia)
    finally:
        cursor.close()

def getCountFInicioCurrentMonth():
    cursor = connection.cursor()
    try:
        sentencia = "SELECT COUNT(fecha_inicio) FROM Tarea WHERE to_char(fecha_inicio, 'MONTH') = to_char(CURRENT_DATE, 'MONTH')"
        cursor.execute(sentencia)
    except Exception as e:
        print("ERROR: ", e, "\nSentencia: ", sentencia)
    finally:
        row = cursor.fetchone()
        return row

def getCountFTerminoCurrentMonth():
    cursor = connection.cursor()
    try:
        sentencia = "SELECT COUNT(fecha_termino) FROM Tarea WHERE to_char(fecha_termino, 'MONTH') = to_char(CURRENT_DATE, 'MONTH')"
        cursor.execute(sentencia)
    except Exception as e:
        print("ERROR: ", e, "\nSentencia: ", sentencia)
    finally:
        row = cursor.fetchone()
        return row

def getCountDepartamentoUsuario():
    cursor = connection.cursor()
    try:
        sentencia = "SELECT T1.DEPARTAMENTO, COUNT(T0.RUT_PERSONA) FROM PERSONA T0 INNER JOIN DEPARTAMENTO T1 ON T0.DEPARTAMENTO_ID_DEPARTAMENTO = T1.ID_DEPARTAMENTO WHERE DEPARTAMENTO_ID_DEPARTAMENTO IS NOT NULL GROUP BY T1.DEPARTAMENTO;"
        cursor.execute(sentencia)
    except Exception as e:
        print("ERROR: ", e, "\nSentencia: ", sentencia)
    finally:
        row = cursor.fetchall()
        return row
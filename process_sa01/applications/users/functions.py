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
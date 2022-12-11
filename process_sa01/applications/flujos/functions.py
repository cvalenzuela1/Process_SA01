import datetime
from dateutil.relativedelta import relativedelta

def getCurrentDate():
    current = datetime.date.today()
    return current

def calcularProximaEjecucionFlujo(tipo_flujo):
    current = datetime.date.today()
    if tipo_flujo == '4':
        current = current + relativedelta(days=+1)
    elif tipo_flujo == '3':
        current = current + relativedelta(weeks=+1)
    elif tipo_flujo == '2':
        current = current + relativedelta(months=+1)
    elif tipo_flujo == '1':
        current = current + relativedelta(years=+1)
    return current
import hashlib
import datetime

def md5DigestHex(text):
    hex_string = hashlib.md5(text.encode("utf-8")).hexdigest()

    return hex_string

def getCurrentDate():
    current = datetime.date.today()
    # current = datetime.datetime.strptime(str(current), '%Y-%m-%d')

    return current
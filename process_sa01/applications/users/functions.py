import hashlib

def md5DigestHex(text):
    hex_string = hashlib.md5(text.encode("utf-8")).hexdigest()

    return hex_string
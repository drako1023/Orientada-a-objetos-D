import re


def validar_texto(texto, longitud_maxima=None, longitud_minima=1):
    if not isinstance(texto, str):
        return False

    texto = texto.strip()
    if len(texto) < longitud_minima:
        return False
    if longitud_maxima is not None and len(texto) > longitud_maxima:
        return False
    return True


def validar_correo(correo):
    if not isinstance(correo, str):
        return False

    correo = correo.strip()
    if len(correo) > 100:
        return False

    patron_correo = r"[A-Za-z0-9.!#$%&'*+/=?^_`{|}~-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)+"
    if re.fullmatch(patron_correo, correo) is None:
        return False

    parte_local = correo.split('@', 1)[0]
    return not parte_local.startswith('.') and not parte_local.endswith('.') and '..' not in parte_local


def validar_contrasenia_segura(contrasenia):
    if not isinstance(contrasenia, str) or any(caracter.isspace() for caracter in contrasenia):
        return False
    if not 8 <= len(contrasenia) <= 15:
        return False

    return (
        re.search(r'[a-z]', contrasenia) is not None
        and re.search(r'[A-Z]', contrasenia) is not None
        and re.search(r'\d', contrasenia) is not None
        and re.search(r'[^\w\s]', contrasenia) is not None
    )


def validar_telefono(telefono):
    if not isinstance(telefono, str):
        return False

    telefono = telefono.strip()
    if not re.fullmatch(r'\+?[0-9][0-9 ()-]*[0-9]', telefono):
        return False

    cantidad_digitos = sum(caracter.isdigit() for caracter in telefono)
    return 7 <= cantidad_digitos <= 15


def validar_entero(valor, minimo=None, maximo=None):
    texto = str(valor).strip() if valor is not None else ''
    if re.fullmatch(r'[+-]?\d+', texto) is None:
        return False

    try:
        numero = int(texto)
    except (TypeError, ValueError):
        return False

    if minimo is not None and numero < minimo:
        return False
    if maximo is not None and numero > maximo:
        return False
    return True


def validar_edad(edad):
    return validar_entero(edad, minimo=0, maximo=120)


def validar_duracion_dias(duracion):
    return validar_entero(duracion, minimo=1)


def validar_opcion(opcion, opciones):
    if opcion is None:
        return False
    return str(opcion).strip() in {str(valor).strip() for valor in opciones}


def validar_si_no(valor):
    if not isinstance(valor, str):
        return False
    return valor.strip().lower() in {'s', 'si', 'sí', 'n', 'no'}
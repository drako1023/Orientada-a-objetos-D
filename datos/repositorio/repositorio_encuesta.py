from datos.modelos.encuesta import Encuesta


def listado_encuestas():
    try:
        encuestas = Encuesta.select().where(Encuesta.activo == 1)
        return list(encuestas)
    except Exception as e:
        print(f"Error al obtener el listado de encuestas: {e}")

def obtener_encuesta_por_titulo(titulo: str):
    try:
        encuesta = Encuesta.get_or_none(Encuesta.titulo == titulo)
        return encuesta
    except Exception as e:
        print(f"Error al obtener la encuesta por titulo: {e}")

def obtener_encuesta_por_id(id_encuesta: int):
    try:
        encuesta = Encuesta.get_or_none(Encuesta.id_encuesta == id_encuesta)
        return encuesta
    except Exception as e:
        print(f"Error al obtener la encuesta por ID: {e}")


def obtener_encuesta_por_privada_permitida():
    try:
        encuestas = Encuesta.select().where(Encuesta.privada_permitida == 1)
        return list(encuestas)
    except Exception as e:
        print(f"Error al obtener la encuesta por privada permitida: {e}")

def guardar_encuesta(encuesta: Encuesta):
    try:
        encuesta_guardada = encuesta.save()
        if encuesta_guardada == 1:
            print(f"Encuesta guardada correctamente: {encuesta}")
    except Exception as e:
        print(f"Error al guardar la encuesta: {e}")               
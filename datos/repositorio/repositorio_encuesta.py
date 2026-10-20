from datos.modelos.py.encuesta import Encuesta


def listado_encuestas():
    try:
        encuestas = Encuestas.select().where(Encuesta.estado == 1)
        if encuestas:
            return list(encuestas)
    except Exception as e:
        print(f"Error al obtener el listado de encuestas: {e}")

def obtener_encuesta_por_id(id_encuesta: int):
    try:
        encuesta = Encuesta.get_or_none(Encuesta.id_encuesta == id_encuesta)
        return encuesta
    except Exception as e:
        print(f"Error al obtener la encuesta por ID: {e}")

def guardar_encuesta(encuesta: Encuesta):
    try:
        encuesta_guardada = encuesta.save()
        if encuesta_guardada == 1:
            print(f"Encuesta guardada correctamente: {encuesta}")
    except Exception as e:
        print(f"Error al guardar la encuesta: {e}")               
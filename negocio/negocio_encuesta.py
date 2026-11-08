
from datos.repositorio.repositorio_encuesta import listado_encuestas

def listado_encuestas(table):
    lista_encuestas = listado_encuestas()
    table.field_names = ["ID", "Nombre", "Descripción", "Fecha de Creación", "Permite privacidad"]
    for encuesta in lista_encuestas:
        table.add_row([encuesta.id, encuesta.titulo, encuesta.descripcion, encuesta.fecha_creacion, encuesta.private_permitida, encuesta.fecha_cierre])
    return table
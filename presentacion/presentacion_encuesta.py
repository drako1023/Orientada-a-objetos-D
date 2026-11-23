
from prettytable import PrettyTable 
from datos.repositorio.repositorio_encuesta import listado_encuestas


def mostrar_encuestas():
    table = PrettyTable()
    table.field_names = [
        "ID",
        "Título",
        "Descripción",
        "Empresa",
        "Recompensa",
        "Fecha de creación",
        "Fecha de cierre",
    ]
    encuestas = listado_encuestas()
    if encuestas is not None:
        for encuesta in encuestas:
            table.add_row([
                encuesta.id_encuesta,
                encuesta.titulo,
                encuesta.descripcion,
                encuesta.id_empresa,
                encuesta.id_recompensa,
                encuesta.fecha_creacion,
                encuesta.fecha_cierre,
            ])
    print(table)
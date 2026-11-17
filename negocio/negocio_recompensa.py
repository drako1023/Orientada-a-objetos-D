

from datos.repositorio.repositorio_recompensa import listado_recompensas

def listado_recompensas(table):
    lista_recompensas = listado_recompensas()
    table.field_names = ["ID", "Reclamada", "Descripción", "Duración", "Requisitos"]
    for recompensa in lista_recompensas:
        table.add_row([recompensa.id_recompensa, recompensa.activo, recompensa.descripcion, recompensa.duracion_dias, recompensa.requisitos])
    return table
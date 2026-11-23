
from prettytable import PrettyTable
from datos.repositorio.repositorio_recompensa import listado_recompensas


def mostrar_recompensas():
    table = PrettyTable()
    table.field_names = [
        "ID",
        "Tipo",
        "Descripción",
        "Duración (días)",
        "Requisitos",
        "Registro requerido",
    ]
    recompensas = listado_recompensas()
    if recompensas is not None:
        for recompensa in recompensas:
            table.add_row([
                recompensa.id_recompensa,
                recompensa.tipo,
                recompensa.descripcion,
                recompensa.duracion_dias,
                recompensa.requisitos,
                recompensa.registro_recompensa,
            ])
    print(table)

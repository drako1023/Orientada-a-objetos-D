
from prettytable import PrettyTable
from datos.repositorio.repositorio_recompensa import listado_recompensas

def mostrar_recompensas():
    table = PrettyTable()
    table = listado_recompensas(table)
    print(table)

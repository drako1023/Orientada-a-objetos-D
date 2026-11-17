
from prettytable import PrettyTable
from datos.repositorio.repositorio_requisitos import listado_requisitos

def mostrar_requisitos():
    table = PrettyTable()
    table = listado_requisitos(table)
    print(table)
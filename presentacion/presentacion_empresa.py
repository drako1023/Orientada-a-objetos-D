from prettytable import PrettyTable
from datos.repositorio.repositorio_empresa import listado_empresas

def mostrar_empresas():
    table = PrettyTable()
    table = listado_empresas(table)
    print(table)
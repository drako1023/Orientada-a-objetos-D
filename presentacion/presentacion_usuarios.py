from prettytable import PrettyTable
from negocio.repositorio.repositorio_usuario import listado_usuarios

def mostrar_usuarios():
    table = PrettyTable()
    table = listado_usuarios(table)
    print(table)
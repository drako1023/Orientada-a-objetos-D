from prettytable import PrettyTable 
from datos.repositorio.repositorio_encuesta import listado_encuestas

def mostrar_encuestas():
    table = PrettyTable()
    table = listado_encuestas(table)
    print(table)
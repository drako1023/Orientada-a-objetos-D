
from prettytable import PrettyTable
from datos.repositorio.repositorio_empresa import listado_empresas


def mostrar_empresas():
    table = PrettyTable()
    table.field_names = ["ID", "Nombre", "Sector", "Ubicación", "Teléfono", "Correo"]
    empresas = listado_empresas()
    if empresas is not None:
        for empresa in empresas:
            table.add_row([
                empresa.id_empresa,
                empresa.nombre_empresa,
                empresa.mercado_empresa,
                empresa.direccion,
                empresa.telefono,
                empresa.correo_electronico,
            ])
    print(table)
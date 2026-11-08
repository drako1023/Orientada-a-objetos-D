
from datos.repositorio.repositorio_empresa import listado_empresas


def listado_empresas(table):
    lista_empresas = listado_empresas()
    table.field_names = ["ID", "Nombre", "Sector", "Ubicación", "Teléfono", "Correo"]
    for empresa in lista_empresas:
        table.add_row([empresa.id, empresa.nombre, empresa.sector, empresa.direccion, empresa.telefono, empresa.correo_electronico])
    return table
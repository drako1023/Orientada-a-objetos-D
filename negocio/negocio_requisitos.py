
from datos.repositorio.repositorio_requisitos import listado_requisitos

def listado_requisitos(table):
    lista_requisitos = listado_requisitos()
    table.field_names = ["ID", "Descripción", "Vínculo", "Activo"]
    for requisito in lista_requisitos:
        table.add_row([requisito.id, requisito.descripcion, requisito.vinculo, requisito.activo])
    return table
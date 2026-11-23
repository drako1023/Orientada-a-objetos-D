
from prettytable import PrettyTable
from datos.repositorio.repositorio_requisitos import listado_requisitos


def mostrar_requisitos():
    table = PrettyTable()
    table.field_names = ["ID", "Descripción", "Vínculo"]
    requisitos = listado_requisitos()
    if requisitos is not None:
        for requisito in requisitos:
            table.add_row([
                requisito.id_requisitos,
                requisito.descripcion,
                requisito.vinculo,
            ])
    print(table)
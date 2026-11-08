
from datos.repositorio.repositorio_usuario import listado_usuarios

def listado_usuarios(table):
    lista_usuarios = listado_usuarios()
    table.field_names = ["ID", "Nombre", "Correo", "Teléfono", "Tipo de Usuario", "Empresa", "Vínculos", "Edad"]
    for usuario in lista_usuarios:
        table.add_row([usuario.id, usuario.nombre, usuario.correo_electronico, usuario.telefono, usuario.tipo_usuario, usuario.empresa, usuario.vinculo, usario.edad])
    return table
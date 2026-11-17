from datos.repositorio.repositorio_usuario import listado_usuarios

def lista_usuarios(table):
    lista_usuarios = listado_usuarios()
    table.field_names = ["ID", "Nombre", "Correo", "Teléfono", "Tipo de Usuario", "Empresa", "Vínculos", "Edad"]
    if lista_usuarios is not None:
        
        for usuario in lista_usuarios:
            table.add_row([usuario.id, usuario.nombre, usuario.correo_electronico, usuario.telefono, usuario.tipo_usuario, usuario.empresa, usuario.vinculo, usuario.edad])
    return table

from datos.modelos.usuario import Usuario
from datos.repositorio.repositorio_usuario import (
    guardar_usuario,
    listado_usuarios,
    obtener_usuario_por_correo_electronico,
)


def lista_usuarios(table):
    usuarios = listado_usuarios()
    table.field_names = [
        "ID",
        "Nombre",
        "Correo",
        "Teléfono",
        "Tipo de Usuario",
        "Empresa",
        "Vínculos",
        "Edad",
    ]

    if usuarios is not None:
        for usuario in usuarios:
            table.add_row([
                usuario.id_usuario,
                usuario.nombre,
                usuario.correo_electronico,
                usuario.telefono,
                usuario.tipo,
                usuario.empresa,
                usuario.vinculo,
                usuario.edad,
            ])
    return table


def obtener_usuario_por_correo(correo):
    return obtener_usuario_por_correo_electronico(correo)


def crear_usuario(nombre, correo, telefono, tipo, empresa, vinculo, edad, contrasenia):
    usuario = Usuario(
        nombre=nombre,
        correo_electronico=correo,
        telefono=telefono,
        tipo=tipo,
        empresa=empresa,
        vinculo=vinculo,
        edad=edad,
        contraseña=contrasenia,
    )
    guardar_usuario(usuario)
    return usuario


def modificar_usuario(
    usuario,
    nombre=None,
    correo=None,
    telefono=None,
    tipo=None,
    empresa=None,
    vinculo=None,
    edad=None,
    contrasenia=None,
):
    if nombre is not None:
        usuario.nombre = nombre
    if correo is not None:
        usuario.correo_electronico = correo
    if telefono is not None:
        usuario.telefono = telefono
    if tipo is not None:
        usuario.tipo = tipo
    if empresa is not None:
        usuario.empresa = empresa
    if vinculo is not None:
        usuario.vinculo = vinculo
    if edad is not None:
        usuario.edad = edad
    if contrasenia is not None:
        usuario.contraseña = contrasenia

    guardar_usuario(usuario)
    return usuario

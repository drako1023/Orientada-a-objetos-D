from datos.modelos.usuario import Usuario

def listado_usuarios():
    try:
        usuarios = Usuario.select().where(Usuario.activo == 1)
        return list(usuarios)
    except Exception as e:
        print(f"Error al obtener el listado de usuarios: {e}")

def obtener_usuario_por_nombre(nombre_usuario: str):
    try:
        usuario = Usuario.get_or_none(Usuario.nombre == nombre_usuario)
        return usuario
    except Exception as e:
        print(f"Error al obtener el usuario por nombre: {e}")

def obtener_usuario_por_id(id_usuario: int):
    try:
        usuario = Usuario.get_or_none(Usuario.id_usuario == id_usuario)
        return usuario
    except Exception as e:
        print(f"Error al obtener el usuario por ID: {e}")

def obtener_usuario_por_correo_electronico(correo_electronico: str):
    try:
        usuario = Usuario.get_or_none(Usuario.correo_electronico == correo_electronico)
        return usuario
    except Exception as e:
        print(f"Error al obtener el usuario por correo electrónico: {e}")

def obtener_usuario_por_tipo(tipo: str):
    try:
        usuarios = Usuario.select().where(Usuario.tipo == tipo)
        return list(usuarios)
    except Exception as e:
        print(f"Error al obtener el usuario por tipo: {e}")


def guardar_usuario(usuario: Usuario):
    try:
        usuario_guardado = usuario.save()
        if usuario_guardado == 1:
            print(f"Usuario guardado correctamente: {usuario}")
    except Exception as e:
        print(f"Error al guardar el usuario: {e}")       
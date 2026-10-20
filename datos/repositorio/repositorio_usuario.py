from datos.modelos.py.usuario import Usuario

def listado_usuarios():
    try:
        usuarios = Usuario.select().where(Usuario.estado == 1)
        if usuarios:
            return usuarios
    except Exception as e:
        print(f"Error al obtener el listado de usuarios: {e}")

def obtener_usuario_por_id(id_usuario: int):
    try:
        usuario = Usuario.get_or_none(Usuario.id_usuario == id_usuario)
        return usuario
    except Exception as e:
        print(f"Error al obtener el usuario por ID: {e}")
def guardar_usuario(usuario: Usuario):
    try:
        usuario_guardado = usuario.save()
        if usuario_guardado == 1:
            print(f"Usuario guardado correctamente: {usuario}")
    except Exception as e:
        print(f"Error al guardar el usuario: {e}")       
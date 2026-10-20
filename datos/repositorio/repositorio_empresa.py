from datos.modelos.py.empresa import Empresa


def listado_empresas():
    try:
        empresas = Empresa.select().where(Empresa.estado == 1)
        if empresas:
            return list(empresas)
    except Exception as e:
        print(f"Error al obtener el listado de empresas: {e}")


def obtener_empresa_por_id(id_empresa: int):
    try:
        empresa = Empresa.get_or_none(Empresa.id_empresa == id_empresa)
        return empresa
    except Exception as e:
        print(f"Error al obtener la empresa por ID: {e}")


def guardar_empresa(empresa: Empresa):
    try:
        empresa_guardada = empresa.save()
        if empresa_guardada == 1:
            print(f"Empresa guardada correctamente: {empresa}")
    except Exception as e:
        print(f"Error al guardar la empresa: {e}")
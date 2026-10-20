from datos.modelos.empresa import Empresa


def listado_empresas():
    try:
        empresas = Empresa.select().where(Empresa.activo == 1)
        return list(empresas)
    except Exception as e:
        print(f"Error al obtener el listado de empresas: {e}")

def obtener_empresa_por_nombre(nombre_empresa: str):
    try:
        empresa = Empresa.get_or_none(Empresa.nombre_empresa == nombre_empresa)
        return empresa
    except Exception as e:
        print(f"Error al obtener la empresa por nombre: {e}")


def obtener_empresa_por_id(id_empresa: int):
    try:
        empresa = Empresa.get_or_none(Empresa.id_empresa == id_empresa)
        return empresa
    except Exception as e:
        print(f"Error al obtener la empresa por ID: {e}")

def obtener_empresa_por_mercado_empresa(mercado_empresa: str):
    try:
        empresas = Empresa.select().where(Empresa.mercado_empresa == mercado_empresa)
        return list(empresas)
    except Exception as e:
        print(f"Error al obtener la empresa por mercado: {e}")



def guardar_empresa(empresa: Empresa):
    try:
        empresa_guardada = empresa.save()
        if empresa_guardada == 1:
            print(f"Empresa guardada correctamente: {empresa}")
    except Exception as e:
        print(f"Error al guardar la empresa: {e}")
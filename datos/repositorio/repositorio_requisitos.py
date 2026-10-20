from datos.modelos.resquisitos import requisitos as Requisito

def listado_requisitos():
    try:
        requisitos = Requisito.select().order_by(Requisito.id_requisitos)
        return list(requisitos)
    except Exception as e:
        print(f"Error al obtener el listado de requisitos: {e}")


def obtener_requisito_por_id(id_requisitos: int):
    try:
        requisito = Requisito.get_or_none(Requisito.id_requisitos == id_requisitos)
        return requisito
    except Exception as e:
        print(f"Error al obtener el requisito por ID: {e}")
       

def guardar_requisito(requisito: Requisito):
    try:
        requisito_guardado = requisito.save()
        if requisito_guardado == 1:
            print(f"Requisito guardado correctamente: {requisito}")
    except Exception as e:
        print(f"Error al guardar el requisito: {e}")
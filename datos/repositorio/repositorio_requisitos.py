from datos.modelos.py.requisito import Requisito

def listado_requisitos():
    try:
        requisitos = Requisito.select().order_by(Requisito.id_requisito)
        if requisitos:
            return list(requisitos)
    except Exception as e:
        print(f"Error al obtener el listado de requisitos: {e}")
def obtener_requisito_por_id(id_requisito: int):
    try:
        requisito = Requisito.get_or_none(Requisito.id_requisito == id_requisito)
        return requisito
    except Exception as e:
        print(f"Error al obtener el requisito por ID: {e}")
       
def guardar_requisito(requisito: Requisito):
    try:
        guardar_requisito = requisito.save()
        if pais_guardado == 1:
            print(f"Requisito guardado correctamente: {requisito}")
    except Exception as e:
        print(f"Error al guardar el requisito: {e}")
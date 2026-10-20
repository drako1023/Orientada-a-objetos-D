from datos.modelos.recompensa import Recompensa


def listado_recompensas():
    try:
        recompensas = Recompensa.select().order_by(Recompensa.id_recompensa)
        return list(recompensas)
    except Exception as e:
        print(f"Error al obtener el listado de recompensas: {e}")


def obtener_recompensa_por_id(id_recompensa: int):
    try:
        recompensa = Recompensa.get_or_none(Recompensa.id_recompensa == id_recompensa)
        return recompensa
    except Exception as e:
        print(f"Error al obtener la recompensa por ID: {e}")


def guardar_recompensa(recompensa: Recompensa):
    try:
        recompensa_guardada = recompensa.save()
        if recompensa_guardada == 1:
            print(f"Recompensa guardada correctamente: {recompensa}")
    except Exception as e:
        print(f"Error al guardar la recompensa: {e}")

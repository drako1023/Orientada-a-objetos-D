from presentacion.presentacion_empresa import mostrar_empresas
from presentacion.presentacion_usuarios import mostrar_usuarios
from presentacion.presentacion_requisitos import mostrar_requisitos
from presentacion.presentacion_recompensa import mostrar_recompensas
from presentacion.presentacion_encuesta import mostrar_encuestas
from auxiliares.auxiliar import main_menu
from auxiliares.validaciones import validar_opcion


def menu_rey():
    while True:
        print("=== Menú de opciones ===")
        for opcion, descripcion in main_menu.items():
            print(f"{opcion}. {descripcion}")

        opcion = input("Seleccione una opción: ")
        if not validar_opcion(opcion, main_menu):
            print("Opción inválida. Por favor, seleccione una opción válida.")
            continue

        if opcion == "1":
            mostrar_empresas()
        elif opcion == "2":
            mostrar_usuarios()
        elif opcion == "3":
            mostrar_requisitos()
        elif opcion == "4":
            mostrar_recompensas()
        elif opcion == "5":
            mostrar_encuestas()
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
from presentacion.presentacion_empresa import mostrar_empresas
from presentacion.presentacion_usuarios import mostrar_usuarios
from presentacion.presentacion_requisitos import mostrar_requisitos
from presentacion.presentacion_recompensa import mostrar_recompensas
from presentacion.presentacion_encuesta import mostrar_encuestas


def menu_rey():
    while True:
        print("=== Menú de opciones ===")
        print("1. Mostrar listado de empresas")
        print("2. Mostrar listado de usuarios")
        print("3. Mostrar listado de requisitos")
        print("4. Mostrar listado de recompensas")
        print("5. Mostrar listado de encuestas")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

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
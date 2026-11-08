from presentacion.presentacion_empresa import mostrar_empresas

def menu_rey():
    while True:
        print("=== Menú de opciones ===")
        print("1. Mostrar listado de empresas")
        print("2. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_empresas()
        elif opcion == "2":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
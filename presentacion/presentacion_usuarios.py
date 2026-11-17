from datos.modelos import usuario
from prettytable import PrettyTable
from negocio.negoicio_usuario import lista_usuarios
from presentacion.menu import menu_rey

def mostrar_usuarios():
    table = PrettyTable()
    table = lista_usuarios(table)
    print(table)

def datos_usuario():
    contrasenia = nombre_usuario = correo_electronico = telefono = tipo_usuario = empresa = vinculo = edad = None
    contrasenia = input("Ingrese datos del usuario:\nContraseña: ")

    while nombre_usuario == None:
        nombre_usuario = input('Nombre: ')

    while correo_electronico == None:
        correo_electronico = input('Correo: ')

    while telefono == None:
        telefono = input('Teléfono: ')

    while tipo_usuario == None:
        tipo_usuario = input('Tipo de Usuario: ')

    while empresa == None:
        empresa = input('Empresa: ')

    while vinculo == None:
        vinculo = input('Vínculo: ')

    while edad == None:
        edad = input('Edad: ')


nombre_usuario = input('Nombre: ')
tabla_usuarios = PrettyTable()
tabla_usuarios = buscar_usuario(tabla_usuarios, nombre_usuario, correo_electronico, telefono, tipo_usuario, empresa, vinculo, edad)                            
print(tabla_usuarios)
id_usuario = input("Ingrese datos del usuario:\nID: ")


def login_usuario():
    while True:
        print(f'\n{nombre_app} {version_app}')
        print('='*len(nombre_app) + "=" + '='*len(version_app))
        print('\nIngrese los datos de\nInicio de Sesión')
        
        correo_electronico = ''
        while correo_electronico == '':
            correo_electronico = input('Correo: ')
            if not validar_correo(correo_electronico):
                print('Correo electrónico NO corresponde, ingrese nuevamente...')
                correo_electronico = ''
            else:
                usuario = usuario_por_correo(correo_electronico)
                if usuario:
                    contrasenia = input('Contraseña: ')
                    
                    if bcrypt.checkpw(contrasenia.encode(), usuario.password):
                        print("¡Contraseña Correcta!")
                        menu_rey()
                    else:
                        print("Contraseña incorrecta,\n ingrese nuevamente...")
                else:
                    print('Usuario no registrado.\n¿Desea registrarse?')
                    opcion_registro = input('Ingrese Si/No [s-n]: ')
                    
                    match opcion_registro.lower():
                        case 's':
                            datos_usuario()
                        case 'n':
                            print('¡Hasta luego!')
                            break

from prettytable import PrettyTable

from auxiliares.auxiliar import nombre_app, version_app
from auxiliares.validaciones import (
    validar_contrasenia_segura,
    validar_correo,
    validar_edad,
    validar_si_no,
    validar_telefono,
    validar_texto,
)
from datos.modelos.usuario import Usuario
from datos.repositorio.repositorio_usuario import (
    guardar_usuario,
    obtener_usuario_por_correo_electronico,
)
from negocio.negoicio_usuario import lista_usuarios

def mostrar_usuarios():
    table = PrettyTable()
    table = lista_usuarios(table)
    print(table)

def datos_usuario():
    contrasenia = input("Contraseña (8-15 caracteres): ")
    while not validar_contrasenia_segura(contrasenia):
        print('Contraseña insegura. Debe incluir mayúscula, minúscula, número y símbolo.')
        contrasenia = input("Contraseña (8-15 caracteres): ")

    nombre = input('Nombre: ')
    while not validar_texto(nombre, longitud_maxima=50):
        print('El nombre debe tener entre 1 y 50 caracteres.')
        nombre = input('Nombre: ')

    correo = input('Correo: ')
    while not validar_correo(correo):
        print('Correo electrónico NO corresponde, ingrese nuevamente...')
        correo = input('Correo: ')

    telefono = input('Teléfono: ')
    while not validar_telefono(telefono):
        print('Teléfono NO corresponde, ingrese nuevamente...')
        telefono = input('Teléfono: ')

    tipo = input('Tipo de Usuario: ')
    while not validar_texto(tipo, longitud_maxima=20):
        print('El tipo debe tener entre 1 y 20 caracteres.')
        tipo = input('Tipo de Usuario: ')

    empresa = input('Empresa: ')
    while not validar_texto(empresa, longitud_maxima=100):
        print('La empresa debe tener entre 1 y 100 caracteres.')
        empresa = input('Empresa: ')

    vinculo = input('Vínculo: ')
    while not validar_texto(vinculo, longitud_maxima=20):
        print('El vínculo debe tener entre 1 y 20 caracteres.')
        vinculo = input('Vínculo: ')

    edad = input('Edad: ')
    while not validar_edad(edad):
        print('La edad debe ser un número entre 0 y 120.')
        edad = input('Edad: ')

    nuevo_usuario = Usuario(
        contraseña=contrasenia,
        correo_electronico=correo.strip(),
        edad=int(edad),
        empresa=empresa.strip(),
        nombre=nombre.strip(),
        telefono=telefono.strip(),
        tipo=tipo.strip(),
        vinculo=vinculo.strip(),
    )
    guardar_usuario(nuevo_usuario)


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
                usuario = obtener_usuario_por_correo_electronico(correo_electronico.strip())
                if usuario:
                    contrasenia = input('Contraseña: ')

                    if contrasenia == usuario.contraseña:
                        print("¡Contraseña Correcta!")
                        from presentacion.menu import menu_rey
                        menu_rey()
                    else:
                        print("Contraseña incorrecta,\n ingrese nuevamente...")
                else:
                    print('Usuario no registrado.\n¿Desea registrarse?')
                    opcion_registro = input('Ingrese Si/No [s-n]: ')

                    if validar_si_no(opcion_registro) and opcion_registro.strip().lower() in {'s', 'si', 'sí'}:
                        datos_usuario()
                    elif validar_si_no(opcion_registro):
                        print('¡Hasta luego!')
                        break
                    else:
                        print('Respuesta no válida.')

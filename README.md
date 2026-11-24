# Encuestas Geniales

## Integrantes

- Vicente Muñoz
- Francisco

## Descripción general

Encuestas Geniales es una aplicación de consola desarrollada en Python para la
gestión de encuestas. Permite administrar usuarios, empresas, requisitos,
recompensas y encuestas, además de consultar la información mediante tablas y
aplicar filtros según las operaciones disponibles en el menú.

Los datos se almacenan en una base de datos MySQL y el acceso a ellos se realiza
mediante Peewee como ORM.

## Dependencias

- Python 3
- MySQL Server
- Peewee
- PyMySQL
- PrettyTable

## Procedimiento de instalación

1. Instale Python 3 y MySQL Server.
2. Clone el proyecto y abra una terminal dentro de su carpeta.
3. Cree y active un entorno virtual:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

4. Instale las bibliotecas necesarias:

```powershell
pip install peewee pymysql prettytable
```

Para repetir la instalación desde otro equipo, puede guardarse un archivo
`requirements.txt` con esas tres bibliotecas y ejecutar:

```powershell
pip install -r requirements.txt
```

## Procedimiento de creación de la base de datos

La base de datos se puede crear fácilmente con XAMPP y phpMyAdmin.

1. Instale XAMPP y abra el **Panel de control de XAMPP**.
2. Inicie los servicios **Apache** y **MySQL**.
3. Abra phpMyAdmin desde `http://localhost/phpmyadmin`.
4. Cree una base de datos llamada `encuestas` con cotejamiento
   `utf8mb4_unicode_ci`.
5. Seleccione la base `encuestas`, abra la pestaña **Usuario** o **Privilegios**
   según la versión de phpMyAdmin y cree el usuario de la aplicación con:
   - Usuario: `chile`
   - Host: `localhost`
   - Contraseña: `1234`
6. Asigne al usuario todos los permisos sobre la base `encuestas`.

También puede ejecutar el siguiente bloque desde la pestaña **SQL** de phpMyAdmin:

```sql
CREATE DATABASE encuestas
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

CREATE USER IF NOT EXISTS 'chile'@'localhost' IDENTIFIED BY '1234';
GRANT ALL PRIVILEGES ON encuestas.* TO 'chile'@'localhost';
FLUSH PRIVILEGES;
```

7. Seleccione la base `encuestas` y abra la pestaña **Importar**.
8. Pulse **Seleccionar archivo**, elija `datos/sql/encuestas.sql` y confirme
   con **Importar**.
9. Compruebe que se hayan creado las tablas `usuario`, `empresa`,
   `recompensa`, `encuesta` y `requisitos`.

La configuración predeterminada de la aplicación utiliza:

- Base de datos: `encuestas`
- Host: `localhost`
- Puerto: `3306`
- Usuario: `chile`
- Contraseña: `1234`

Si su usuario o contraseña de MySQL son distintos, modifique los valores en
`datos/database.py`.

## Usuario inicial

El proyecto no incluye un usuario inicial ni datos precargados. El menú actual
permite consultar los usuarios existentes, pero no contiene una opción para
registrarlos. Para agregar registros, utilice MySQL o un flujo que implemente
`datos_usuario()` desde `presentacion/presentacion_usuarios.py`.

## Instrucciones de ejecución

Desde la carpeta raíz del proyecto y con el entorno virtual activo, ejecute:

```powershell
python app.py
```

La aplicación mostrará el menú principal en la consola. Seleccione una opción
usando su número y siga las indicaciones mostradas en pantalla. Para finalizar,
seleccione la opción de salida del menú.

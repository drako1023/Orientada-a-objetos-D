import os
from pathlib import Path

from peewee import MySQLDatabase


def cargar_entorno(path):
    valores = {}

    if not path.exists():
        return valores

    with path.open("r", encoding="utf-8") as archivo:
        for linea in archivo:
            linea = linea.strip()
            if not linea or linea.startswith("#") or "=" not in linea:
                continue

            clave, valor = linea.split("=", 1)
            valor = valor.strip()
            if len(valor) >= 2 and valor[0] == valor[-1] and valor[0] in ("'", '"'):
                valor = valor[1:-1]
            valores[clave.strip()] = valor

    return valores


directorio_raiz = Path(__file__).resolve().parent.parent
entorno = cargar_entorno(directorio_raiz / ".env")


def obtener_configuracion(clave, valor_predeterminado):
    return os.environ.get(clave, entorno.get(clave, valor_predeterminado))


database = MySQLDatabase(
    obtener_configuracion("DB_NAME", "encuestas"),
    **{
        "charset": obtener_configuracion("DB_CHARSET", "utf8mb4"),
        "host": obtener_configuracion("DB_HOST", "localhost"),
        "port": int(obtener_configuracion("DB_PORT", "3306")),
        "user": obtener_configuracion("DB_USER", "chile"),
        "password": obtener_configuracion("DB_PASSWORD", "1234"),
    },
)

from peewee import *


database = MySQLDatabase(
    'encuestas',
    **{'charset': 'utf8mb4', 'host': 'localhost', 'port': 3306, 'user': 'chile', 'password': '1234'}
)


class BaseModel(Model):
    class Meta:
        database = database

class Usuario(BaseModel):
    activo = BooleanField(constraints=[SQL("DEFAULT 1")], null=True)
    contraseña = charField()
    correo_electronico = CharField(max_length=100, unique=True)
    edad = IntegerField(null=True)
    empresa = CharField(max_length=100, null=True)
    fecha_registro = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    id_usuario = IntegerField(primary_key=True)
    nombre = CharField(max_length=100)
    telefono = CharField(max_length=15, null=True)
    tipo = CharField(max_length=20, null=True)
    vinculo = CharField(max_length=20, null=True)

    class Meta:
        table_name = 'usuario'


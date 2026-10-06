from peewee import *


database = MySQLDatabase(
    'encuestas',
    **{'charset': 'utf8mb4', 'host': 'localhost', 'port': 3306, 'user': 'chile', 'password': '1234'}
)


class BaseModel(Model):
    class Meta:
        database = database


class Recompensa(BaseModel):
    activo = BooleanField(constraints=[SQL("DEFAULT 1")], null=True)
    descripcion = CharField(null=True)
    duracion_dias = IntegerField(null=True)
    id_recompensa = IntegerField(primary_key=True)
    registro_recompensa = BooleanField(constraints=[SQL("DEFAULT 1")], null=True)
    requisitos = CharField(null=True)
    tipo = CharField(max_length=50)

    class Meta:
        table_name = 'recompensa'


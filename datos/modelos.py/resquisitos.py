from peewee import *


database = MySQLDatabase(
    'encuestas',
    **{'charset': 'utf8mb4', 'host': 'localhost', 'port': 3306, 'user': 'chile', 'password': '1234'}
)

class BaseModel(Model):
    class Meta:
        database = database


class requisitos(BaseModel):
    activo = BooleanField(constraints=[SQL("DEFAULT 1")], null=True)
    descripcion = CharField(null=True)
    id_requisitos = IntegerField(primary_key=True)
    vinculo = CharField(max_length=20, null=True)

    class Meta:
        table_name = 'requisitos'
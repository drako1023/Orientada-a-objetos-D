from peewee import *


database = MySQLDatabase(
    'encuestas',
    **{'charset': 'utf8mb4', 'host': 'localhost', 'port': 3306, 'user': 'chile', 'password': '1234'}
)


class BaseModel(Model):
    class Meta:
        database = database


class Encuesta(BaseModel):
    activo = BooleanField(constraints=[SQL("DEFAULT 1")], null=True)
    descripcion = TextField()
    fecha_cierre = DateTimeField(null=True)
    fecha_creacion = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    grupo_interes = CharField(max_length=100, null=True)
    id_empresa = IntegerField(index=True)
    id_encuesta = IntegerField(primary_key=True)
    id_recompensa = IntegerField(index=True, null=True)
    id_usuario = IntegerField(index=True, null=True)
    privada_permitida = BooleanField(constraints=[SQL("DEFAULT 0")], null=True)
    titulo = CharField(max_length=100)

    class Meta:
        table_name = 'encuesta'




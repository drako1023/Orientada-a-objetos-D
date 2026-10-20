from peewee import BooleanField, CharField, DateTimeField, IntegerField, Model, SQL

from datos.database import database


class BaseModel(Model):
    class Meta:
        database = database

class Usuario(BaseModel):
    activo = BooleanField(constraints=[SQL("DEFAULT 1")], null=True)
    contraseña = CharField()
    correo_electronico = CharField(max_length=100, unique=True)
    edad = IntegerField(null=True)
    empresa = CharField(max_length=100, null=True)
    fecha_registro = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    id_usuario = IntegerField(primary_key=True)
    nombre = CharField(max_length=50)
    telefono = CharField(max_length=15, null=True)
    tipo = CharField(max_length=20, null=True)
    vinculo = CharField(max_length=20, null=True)

    class Meta:
        table_name = 'usuario'

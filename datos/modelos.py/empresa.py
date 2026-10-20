from peewee import BooleanField, CharField, DateTimeField, IntegerField, Model, SQL

from datos.database import database


class BaseModel(Model):
    class Meta:
        database = database


class Empresa(BaseModel):
    activo = BooleanField(constraints=[SQL("DEFAULT 1")], null=True)
    correo_electronico = CharField(max_length=100, unique=True)
    direccion = CharField(null=True)
    fecha_registro = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    id_empresa = IntegerField(primary_key=True)
    mercado_empresa = CharField(max_length=100, null=True)
    nombre_empresa = CharField(max_length=100)
    telefono = CharField(max_length=15, null=True)

    class Meta:
        table_name = 'empresa'

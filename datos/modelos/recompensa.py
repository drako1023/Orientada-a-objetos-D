from peewee import BooleanField, CharField, IntegerField, Model, SQL

from datos.database import database


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

from django.db import models

# Create your models here.


class clientes(models.Model):
    idClientes = models.IntegerField(primary_key=True, db_column='idClientes')
    Nombre = models.CharField(max_length=100,db_column='Nombre')
    Apellido = models.CharField(max_length=100, db_column='Apellido')
    Correo_Electronico = models.CharField(max_length=100, db_column='Correo Electronico')
    Telefono = models.IntegerField(db_column= 'Telefono')
    class Meta:
        db_table = 'clientes'
        
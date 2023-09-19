from django.db import models

# Create your models here.


class clientes(models.Model):
    ID_Clientes = models.IntegerField(primary_key=True, db='ID_Clientes')
    Nombre = models.CharField(max_length=100,db_column='Nombre')
    Apellido = models.CharField(max_length=100, db_column='Apellido')
    Correo_Electronico = models.CharField(max_length=100, db_column='Correo Electronico')
    Telefono = models.IntegerChoices(max_length=10, db_column= 'Telefono')
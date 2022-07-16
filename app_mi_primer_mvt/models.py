from django.db import models

class concesionario(models.Model):
    Marca= models.CharField(max_length=20)
    Modelo= models.CharField(max_length=20)
    Valor= models.IntegerField()

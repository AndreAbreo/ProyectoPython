from django.db import models


# Create your models here.
class Producto(models.Model):
   
    nombre = models.CharField(max_length=30)
    precio = models.FloatField()
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Heroe(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    imagen = models.URLField()
    historia = models.TextField(max_length=400)
    
    def __str__(self):
        return self.nombre 

class Usuario(models.Model):
    alias = models.CharField(max_length=30)
    personaje_fav =  models.CharField(max_length=50)
    telefono = models.FloatField()
    codigo = models.CharField(max_length=30)

    def __str__(self):
        return self.alias
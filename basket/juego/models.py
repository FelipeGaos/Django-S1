from django.db import models

# Create your models here.


class jugador(models.Model):
    nombre = models.CharField(max_length=200)
    apodo = models.CharField(max_length=50)
    fecha_nac = models.DateField()
    edad = models.IntegerField()
    rut = models.IntegerField()
    email = models.EmailField()
    estatura = models.FloatField()
    peso = models.IntegerField()
    foto = models.ImageField(upload_to = 'img/', default = 'img/None/no-img.jpg')
    poscicion = models.CharField(max_length=50)
    

class equipo(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    logo = models.ImageField(upload_to = 'img/', default = 'img/None/no-img.jpg')



class entrenador(models.Model):
    nombre = models.CharField(max_length=200)
    apodo = models.CharField(max_length=50)
    edad = models.IntegerField()
    rut = models.IntegerField()
    email = models.EmailField()

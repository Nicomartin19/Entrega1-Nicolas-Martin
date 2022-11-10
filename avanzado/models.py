from pyexpat import model
from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.

class Mascota(models.Model):
    nombre = models.CharField(max_length = 20)
    tipo = models.CharField(max_length = 20)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()
    descripcion = RichTextField(null=True)
    
    def __str__(self):
        return f"Nombre: {self.nombre} - Tipo: {self.tipo}"
    

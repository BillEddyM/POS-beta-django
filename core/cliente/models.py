from django.db import models

# Create your models here.
class Cliente(models.Model):
    cliente_id = models.CharField(max_length=100, primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    nit = models.CharField(max_length=100, default='c/f')
    telefono = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"



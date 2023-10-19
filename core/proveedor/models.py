from django.db import models

# Create your models here.
class Proveedor(models.Model):
    proveedor_id = models.CharField(max_length=100, primary_key=True)
    nombre = models.CharField(max_length=100)
    nit = models.CharField(max_length=100, default='c/f')
    tipo_producto = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.nombre}"



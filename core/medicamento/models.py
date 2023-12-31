from django.db import models

from proveedor.models import Proveedor


class Laboratorio(models.Model):
    laboratorio_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Laboratorios"

class Categoria(models.Model):
    categoria_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Categorías"

class Medicamento(models.Model):
    medicamento_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio_compra = models.DecimalField(max_digits=5, decimal_places=2) 
    precio_venta = models.DecimalField(max_digits=5, decimal_places=2) 
    stock = models.IntegerField()
    fecha_expiracion = models.DateField()
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='imagenes', null=True, blank=True)


    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Medicamentos"

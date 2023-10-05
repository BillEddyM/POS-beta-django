from django.db import models

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
    stock = models.IntegerField()
    fecha_expiracion = models.DateField()
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    
    

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Medicamentos"

from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Venta, DetalleVenta

class VentaAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'fecha_venta', 'total')
    list_filter = ('cliente', 'fecha_venta')
    search_fields = ('cliente__nombre', 'cliente__apellido', 'cliente__cliente_id')
    date_hierarchy = 'fecha_venta'

class DetalleVentaAdmin(admin.ModelAdmin):
    list_display = ('id', 'venta', 'medicamento', 'cantidad', 'precio_unitario', 'sub_total')
    list_filter = ('venta', 'medicamento')
    search_fields = ('venta__id', 'medicamento__nombre')
    date_hierarchy = 'venta__fecha_venta'

admin.site.register(Venta, VentaAdmin)
admin.site.register(DetalleVenta, DetalleVentaAdmin)

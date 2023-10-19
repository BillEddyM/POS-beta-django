from django.contrib import admin

# Register your models here.
from .models import Proveedor

class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('proveedor_id', 'nombre', 'telefono')
    search_fields = ('proveedor_id', 'nombre', 'nit')

admin.site.register(Proveedor, ProveedorAdmin)


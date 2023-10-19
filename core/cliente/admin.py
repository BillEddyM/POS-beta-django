from django.contrib import admin
from .models import Cliente

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('cliente_id', 'nombre', 'apellido' , 'nit', 'telefono')
    search_fields = ('cliente_id', 'nombre', 'apellido' , 'nit', 'telefono')
    list_filter = ('cliente_id', 'nombre', 'apellido' , 'nit')

admin.site.register(Cliente, ClienteAdmin)

from django.contrib import admin

# Register your models here.
from .models import Medicamento, Categoria, Laboratorio

class MedicamentoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'stock', 'laboratorio', 'categoria')
    search_fields = ('nombre', 'descripcion')
    


admin.site.register(Medicamento, MedicamentoAdmin)
admin.site.register(Categoria)
admin.site.register(Laboratorio)

from django.contrib import admin

# Register your models here.
from .models import Medicamento

class MedicamentoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'stock')
    search_fields = ('nombre', 'descripcion')
    list_filter = ('categoria', 'laboratorio')

admin.site.register(Medicamento, MedicamentoAdmin)

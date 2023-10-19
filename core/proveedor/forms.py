from django import forms
from .models import Proveedor

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['proveedor_id',
                   'nombre',
                    'nit',
                    'tipo_producto']

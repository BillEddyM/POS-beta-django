
from django import forms
from django.forms import inlineformset_factory
from .models import Venta, DetalleVenta

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['cliente']

DetalleVentaFormSet = inlineformset_factory(
        Venta,
        DetalleVenta,
        fields=['medicamento', 'cantidad', 'sub_total'],
        extra=3
)


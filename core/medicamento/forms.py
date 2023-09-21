from django import forms

from .models import Medicamento, Categoria, Laboratorio

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['categoria_id', 'nombre']


class LaboratorioForm(forms.ModelForm):
    class Meta:
        model = Laboratorio
        fields = ['laboratorio_id','nombre']
        
class MedicamentoForm(forms.ModelForm):
    class Meta:
        model = Medicamento  # Especifica el modelo al que está vinculado este formulario
        fields = '__all__'  
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'fecha_expiracion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'laboratorio': forms.Select(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
        }

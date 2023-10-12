from django.shortcuts import render

from django.shortcuts import render, redirect
from .models import Cliente, Venta, DetalleVenta
from .forms import VentaForm, DetalleVentaFormSet
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


from django.urls import reverse_lazy  #PARA EL REDIRECCIONAMIENTO AUTOMATICO
from django.forms.models import inlineformset_factory #inlines

class VentaListView(ListView):
    model = Venta
    template_name = 'venta/venta_list.html'
    context_object_name = 'ventas'

class VentaCreateView(CreateView):
    model = Venta
    form_class = VentaForm
    template_name = 'venta/crear_venta.html'
    success_url = reverse_lazy('venta_list')

    def get_context_data(self, **kwargs):
        data = super(VentaCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            data['detalle_formset'] = DetalleVentaFormSet(self.request.POST)
        else:
            data['detalle_formset'] = DetalleVentaFormSet()
        data['medicamentos'] = Medicamento.objects.all()
        return data
    
    def get_context_data(self, **kwargs):
        data = super(VentaListView, self).get_context_data(**kwargs)
        data['medicamentos'] = Medicamento.objects.all()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        detalle_formset = context['detalle_formset']
        with transaction.atomic():
            form.instance.usuario = self.request.user
            self.object = form.save()
            if detalle_formset.is_valid():
                detalle_formset.instance = self.object
                detalle_formset.save()
        return super(VentaCreateView, self).form_valid(form)



from django.shortcuts import render
# Create your views here.
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Medicamento, Categoria, Laboratorio
from django.db.models import Q
from .forms import MedicamentoForm, CategoriaForm, LaboratorioForm

from django.urls import reverse_lazy  #PARA EL REDIRECCIONAMIENTO AUTOMATICO

#imports necesarias para la api 
from rest_framework import viewsets
from .models import Medicamento
from .serializers import MedicamentoSerializer
from django.contrib.auth.mixins import PermissionRequiredMixin

class MedicamentoListView(PermissionRequiredMixin, ListView):
    permission_required = 'medicamento.view_medicamento'
    model = Medicamento
    template_name = 'medicamento/medicamento_list.html'
    context_object_name = 'medicamentos'
    
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Medicamento.objects.filter(Q(nombre__icontains=query) | Q(medicamento_id__icontains=query))
        else:
            return Medicamento.objects.all()

class MedicamentoCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'medicamento.add_medicamento'
    model = Medicamento
    form_class = MedicamentoForm
    template_name = 'medicamento/medicamento_form.html'
    success_url = reverse_lazy('medicamento_list')

class MedicamentoUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'medicamento.change_medicamento'
    model = Medicamento
    form_class = MedicamentoForm
    template_name = 'medicamento/medicamento_form.html'
    success_url = reverse_lazy('medicamento_list')

class MedicamentoDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'medicamento.delete_medicamento'
    model = Medicamento
    template_name = 'medicamento/medicamento_confirm_delete.html'
    success_url = reverse_lazy('medicamento_list')

class LaboratorioListView(PermissionRequiredMixin, ListView):
    permission_required = 'medicamento.view_laboratorio'
    model = Laboratorio
    template_name = 'laboratorio/laboratorio_list.html'
    context_object_name = 'laboratorios'
    
    def get_queryset(self): #para la busqueda 
        query = self.request.GET.get('q')
        if query:
            return Laboratorio.objects.filter(Q(nombre__icontains=query) | Q(laboratorio_id__icontains=query))
        else:
            return Laboratorio.objects.all()

class LaboratorioCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'medicamento.add_laboratorio'
    model = Laboratorio
    form_class = LaboratorioForm
    template_name = 'laboratorio/laboratorio_form.html'
    success_url = reverse_lazy('laboratorio_list') #para regresar al listado 

class LaboratorioUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'medicamento.change_laboratorio'
    model = Laboratorio
    form_class = LaboratorioForm
    template_name = 'laboratorio/laboratorio_form.html'
    success_url = reverse_lazy('laboratorio_list')

class LaboratorioDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'medicamento.delete_laboratorio'
    model = Laboratorio
    template_name = 'laboratorio/laboratorio_confirm_delete.html'
    success_url = reverse_lazy('laboratorio_list')

class CategoriaListView(PermissionRequiredMixin, ListView):
    permission_required = 'medicamento.view_categoria'
    model = Categoria
    template_name = 'categoria/categoria_list.html'
    context_object_name = 'categorias'
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Categoria.objects.filter(Q(nombre__icontains=query) | Q(cotegoria_id__icontains=query))
        else:
            return Categoria.objects.all()

class CategoriaCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'medicamento.add_categoria'
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categoria/categoria_form.html'
    success_url = reverse_lazy('categoria_list')

class CategoriaUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'medicamento.change_categoria'
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categoria/categoria_form.html'
    success_url = reverse_lazy('categoria_list')

class CategoriaDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'medicamento.delete_categoria'
    model = Categoria
    template_name = 'categoria/categoria_confirm_delete.html'
    success_url = reverse_lazy('categoria_list')


#   -----------------    vistas para las apis    ----------------------------------------------------

class MedicamentoViewSet(viewsets.ModelViewSet):
    queryset = Medicamento.objects.all()
    serializer_class = MedicamentoSerializer


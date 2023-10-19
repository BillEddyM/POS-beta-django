from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Proveedor
from django.db.models import Q
from .forms import ProveedorForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from rest_framework import viewsets
from rest_framework import serializers

class ProveedorListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Proveedor
    template_name = 'proveedor/proveedor_list.html'
    context_object_name = 'proveedores'
    login_url = '/login/'
    permission_required = 'proveedor.view_proveedor'
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Proveedor.objects.filter(Q(nombre__icontains=query) | Q(nit__icontains=query))
        else:
            return Proveedor.objects.all()

class ProveedorCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Proveedor
    form_class = ProveedorForm
    template_name = 'proveedor/proveedor_form.html'
    success_url = reverse_lazy('proveedor_list')
    login_url = '/login/'
    permission_required = 'proveedor.add_proveedor'

class ProveedorUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Proveedor
    form_class = ProveedorForm
    template_name = 'proveedor/proveedor_form.html'
    success_url = reverse_lazy('proveedor_list')
    login_url = '/login/'
    permission_required = 'proveedor.change_proveedor'

class ProveedorDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Proveedor
    template_name = 'proveedor/proveedor_confirm_delete.html' #direccion del template
    success_url = reverse_lazy('proveedor_list') #para redireccionar automaticamente reverse lazy
    login_url = '/login/'
    permission_required = 'proveedor.delete_proveedor'


class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = '__all__'

class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer


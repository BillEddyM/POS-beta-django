from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Cliente
from django.db.models import Q
from .forms import ClienteForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from rest_framework import viewsets
from rest_framework import serializers

class ClienteListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Cliente
    template_name = 'cliente/cliente_list.html'
    context_object_name = 'clientes'
    login_url = '/login/'
    permission_required = 'cliente.view_cliente'
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Cliente.objects.filter(Q(nombre__icontains=query) | Q(nit__icontains=query))
        else:
            return Cliente.objects.all()

class ClienteCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente/cliente_form.html'
    success_url = reverse_lazy('cliente_list')
    login_url = '/login/'
    permission_required = 'cliente.add_cliente'

class ClienteUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente/cliente_form.html'
    success_url = reverse_lazy('cliente_list')
    login_url = '/login/'
    permission_required = 'cliente.change_cliente'

class ClienteDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Cliente
    template_name = 'cliente/cliente_confirm_delete.html' #direccion del template 
    success_url = reverse_lazy('cliente_list') #para redireccionar automaticamente reverse lazy 
    login_url = '/login/'
    permission_required = 'cliente.delete_cliente'


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


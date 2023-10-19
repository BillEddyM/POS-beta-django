from django.urls import path
from . import views
from rest_framework import routers




urlpatterns = [
    path('', views.ProveedorListView.as_view(), name='proveedor_list'),
    path('proveedor/nuevo/', views.ProveedorCreateView.as_view(), name='proveedor_create'),
    path('proveedor/<int:pk>/', views.ProveedorUpdateView.as_view(), name='proveedor_update'),
    path('proveedor/<int:pk>/eliminar/', views.ProveedorDeleteView.as_view(), name='proveedor_delete'),
]

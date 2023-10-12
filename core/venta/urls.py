from django.urls import path
from . import views

urlpatterns = [
    path('ventas/', views.VentaListView.as_view(), name='venta_list'),
    path('ventas/nueva/', views.VentaCreateView.as_view(), name='crear_venta'),
    #path('ventas/<int:pk>/', views.VentaUpdateView.as_view(), name='venta_update'),
    #path('ventas/<int:pk>/eliminar/', views.VentaDeleteView.as_view(), name='venta_delete'),
]

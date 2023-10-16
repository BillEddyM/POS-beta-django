from django.urls import path

from . import views

urlpatterns = [
    path('lista/', views.lista_ventas, name='listar_ventas'),
    path('realizar_venta/', views.view_crear_venta, name='venta_crear_venta'),
    path('crear_venta_post/', views.crear_venta_post, name='crear_venta_post'),
    path('ver_detalle_venta/<int:id>', views.ver_detalle_venta, name='ver_detalle_venta'),
    #path('ventas/nueva/', views.VentaCreateView.as_view(), name='crear_venta'),
    #path('ventas/<int:pk>/', views.VentaUpdateView.as_view(), name='venta_update'),
    #path('ventas/<int:pk>/eliminar/', views.VentaDeleteView.as_view(), name='venta_delete'),
]

from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('medicamentos/', views.MedicamentoListView.as_view(), name='medicamento_list'),
    path('medicamentos/nuevo/', views.MedicamentoCreateView.as_view(), name='medicamento_create'),
    path('medicamentos/<int:pk>/', views.MedicamentoUpdateView.as_view(), name='medicamento_update'),
    path('medicamentos/<int:pk>/eliminar/', views.MedicamentoDeleteView.as_view(), name='medicamento_delete'),
    path('laboratorios/', views.LaboratorioListView.as_view(), name='laboratorio_list'),
    path('laboratorios/nuevo/', views.LaboratorioCreateView.as_view(), name='laboratorio_create'),
    path('laboratorios/<int:pk>/', views.LaboratorioUpdateView.as_view(), name='laboratorio_update'),
    path('laboratorios/<int:pk>/eliminar/', views.LaboratorioDeleteView.as_view(), name='laboratorio_delete'),
    path('categorias/', views.CategoriaListView.as_view(), name='categoria_list'),
    path('categorias/nuevo/', views.CategoriaCreateView.as_view(), name='categoria_create'),
    path('categorias/<int:pk>/', views.CategoriaUpdateView.as_view(), name='categoria_update'),
    path('categorias/<int:pk>/eliminar/', views.CategoriaDeleteView.as_view(), name='categoria_delete'),
] 


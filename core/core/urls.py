
from django.contrib import admin
from django.urls import path, include

#imports para la api 
from rest_framework import routers
from medicamento.views import MedicamentoViewSet

router = routers.DefaultRouter()
router.register(r'medicamentos', MedicamentoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("home.urls")),
    path('medicamentos/', include("medicamento.urls")),
    #api 
    path('api/', include(router.urls)),
]
    

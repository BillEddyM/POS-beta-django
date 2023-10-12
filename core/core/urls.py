
from django.contrib import admin
from django.urls import path, include

from rest_framework.authtoken.views import obtain_auth_token


#imports para la api 
from rest_framework import routers
from medicamento.views import MedicamentoViewSet

from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'medicamentos', MedicamentoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include("customauthentication.urls")),
    path('', include("home.urls")),
    path('inventario/', include("medicamento.urls")),
    path('clientes/', include("cliente.urls")),
    path('ventas/', include("venta.urls")),
    #api 
    path('api/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


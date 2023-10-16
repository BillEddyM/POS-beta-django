

from django.contrib import admin
from django.urls import path
from .views import HomeTemplateView
from home import views

urlpatterns = [
    path('', views.ver_home, name='home'),
]



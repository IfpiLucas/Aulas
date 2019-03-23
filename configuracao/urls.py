"""configuracao URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('listar', listar, name="url_listar"),
    path('cadastrar', adicionar, name='url_adcionar'),

    #   A seguir temos algumas urls dinâmicas onde passamos
    # um inteiro por parâmetro que neste caso é a chave primária
    # de nosso objeto.
    path('atualizar/<int:pk>', atualizar, name="url_atualizar"),
    path('deletar/<int:pk>', deletar, name="url_deletar")
]

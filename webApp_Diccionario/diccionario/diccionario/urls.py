"""diccionario URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from gestion_diccionario.views import inicio, busqueda, anadirPalabra, success_anadida, eliminarPalabra, success_eliminada,editar_def_paso1, editar_def_paso2, success_editada

urlpatterns = [
    path('admin/', admin.site.urls),
    path("inicio/", inicio),
    path("buscar/", busqueda),
    path("anadirPalabra/", anadirPalabra),
    path("success_anadida/", success_anadida),
    path("eliminarPalabra/", eliminarPalabra),
    path("success_eliminada/", success_eliminada),
    path("editar_def_paso1/", editar_def_paso1),
    path("editar_def_paso2/", editar_def_paso2),
    path("success_editada/", success_editada),
]

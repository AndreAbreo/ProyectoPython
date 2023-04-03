"""crud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from tienda import views
from tienda.views import BuscarProducto, BuscarHeroe, BuscarUsuario
from tienda.forms import BuscarProductoForm, BuscarHeroeForm, BuscarUsuarioForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name ='inicio'),
    path('productos', views.consultar, name = 'consultar'),
    path('productos/guardar', views.guardar, name = 'guardar'),
    path('productos/eliminar/<int:id>', views.eliminar, name = 'eliminar'),
    path('productos/detalle/<int:id>', views.detalle, name = 'detalle'),
    path('productos/editar', views.editar, name = 'editar'),
    path('productos/list', BuscarProducto.as_view(), name="producto-list"),
    path('heroes', views.consultar1, name = 'consultar1'),
    path('heroes/guardar1', views.guardar1, name = 'guardar1'),
    path('heroes/eliminar1/<int:id>', views.eliminar1, name = 'eliminar1'),
    path('heroes/detalle1/<int:id>', views.detalle1, name = 'detalle1'),
    path('heroes/editar1', views.editar1, name = 'editar1'),
    path('heroes/list', BuscarHeroe.as_view(), name="heroe-list"),
    path('usuarios', views.consultar2, name = 'consultar2'),
    path('usuarios/guardar2', views.guardar2, name = 'guardar2'),
    path('usuarios/eliminar2/<int:id>', views.eliminar2, name = 'eliminar2'),
    path('usuarios/detalle2/<int:id>', views.detalle2, name = 'detalle2'),
    path('usuarios/editar2', views.editar2, name = 'editar2'),
    path('usuarios/list', BuscarUsuario.as_view(), name="usuario-list"),

    
]

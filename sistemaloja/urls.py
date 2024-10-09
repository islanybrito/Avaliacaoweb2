
from django.contrib import admin
from django.urls import path, include

from venda.views import listar_clientes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('venda/', include('venda.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('',listar_clientes, name="listar_clientes"),
]

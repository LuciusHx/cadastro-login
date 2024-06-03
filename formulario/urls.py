from django.contrib import admin
from django.urls import path
from usuarios.views import index, login, listagem_usuarios

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('listagem_usuarios/', listagem_usuarios, name='listagem_usuario'),
]


from django.contrib import admin
from django.urls import path,include

#ADICIONE O INCLUDE E PASSE O PATH CONTENDO O NOME DO APP, POR EXEMPLO GALERIA.URLS(NOME DA PASTA)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',include('galeria.urls')),
]

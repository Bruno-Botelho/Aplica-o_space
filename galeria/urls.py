from django.urls import path
from galeria.views import index

# POR BOA PRATICA CRIAMOS UM ARQUIVO DENTRO DO APP QUE IRÁ CONTER TODAS AS ROTAS
# E DEPOIS NAS ROTAS PRINCIPAIS IREMOS CHAMA-LO
urlpatterns = [
    path('', index)
]
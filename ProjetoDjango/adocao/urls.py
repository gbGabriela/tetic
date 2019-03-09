#modulo do django para criar urls
from django.urls import path

#importe toads as suas classes do views.py
from .views import *

urlpatterns = [
    #path('caminho/da/url', ClasseDoView.as_view(), name="nomeDaUrl")
	path('inicio', PaginaInicialView.as_view(), name="index"),
    path('sobre', PaginaSobreView.as_view(), name="sobre"),
]

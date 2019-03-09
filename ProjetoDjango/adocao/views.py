from django.shortcuts import render

from django.views.generic import TemplateView

# Create your views here.
#cria uma classe com herança de TemplateView para exibir um arquivo HTML normal (com o conteúdo dele)
class PaginaInicialView(TemplateView):
    #nome do arquivo que vai ser utilizado para renderizar
    #esta pagina / metodo /classe
    template_name = "index.html"

class PaginaSobreView(TemplateView):
    template_name = "sobre.html"

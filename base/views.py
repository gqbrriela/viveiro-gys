from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'
class ContatosView(TemplateView):
    template_name = 'contatos.html'
class ProdutosView(TemplateView):
    template_name = 'produtos.html'
    
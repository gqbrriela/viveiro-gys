from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HomeView(TemplateView):
    template_name = 'base/pages/home.html'
class ContatosView(TemplateView):
    template_name = 'base/pages/contatos.html'
class ProdutosView(TemplateView):
    template_name = 'base/pages/produtos.html'
    
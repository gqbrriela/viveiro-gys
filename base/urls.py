from django.urls import path
from .views import HomeView, ContatosView, ProdutosView

urlpatterns = [
    path('', HomeView.as_view()),
    path('contatos/', ContatosView.as_view()),
    path('produtos/', ProdutosView.as_view()),


]
from django.urls import path
from .views import HomeView, ContatosView, ProdutosView, CartView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('contatos/', ContatosView.as_view(), name="contatos"),
    path('produtos/', ProdutosView.as_view(), name="produtos"),
    path('cart/', CartView.as_view(), name="cart"),


]
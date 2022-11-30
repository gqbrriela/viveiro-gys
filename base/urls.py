from django.urls import path
from .views import HomeView, ContatosView, SobreView, CartView, register, login


urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('contatos/', ContatosView.as_view(), name="contatos"),
    path('sobre/', SobreView.as_view(), name="sobre"),
    path('cart/', CartView.as_view(), name="cart"),

    #autenticação
    path('cadastro/', register, name = 'cadastro'),
    path('login/', login, name = 'login'),
]


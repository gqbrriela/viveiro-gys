from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.models import User

# Create your views here.

class HomeView(TemplateView):
    template_name = 'base/pages/home.html'
class ContatosView(TemplateView):
    template_name = 'base/pages/contatos.html'
class ProdutosView(TemplateView):
    template_name = 'base/pages/produtos.html'
class CartView(TemplateView):
    template_name = 'base/pages/cart.html'

def register(request):
    if request.method == 'GET':
        return render(request, "base/pages/cadastro.html")
    
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        #user = User.objects.filter('username').first()
        
        #if user:
        #    return render(request, "core/pages/permisson.html")
        #else:
        user = User.objects.create_user(username=username, email=email, password=password)
        
        return render(request, "base/pages/home.html")






    
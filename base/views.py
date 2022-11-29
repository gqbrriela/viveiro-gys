from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from .models import Person

# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'
class ContatosView(TemplateView):
    template_name = 'contatos.html'
class SobreView(TemplateView):
    template_name = 'sobre.html'
class CartView(TemplateView):
    template_name = 'cart.html'

def register(request):
    if request.method == 'GET':
        return render(request, "cadastro.html")
    
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        endereco = request.POST.get('endereco')
        
        #user = User.objects.filter('username').first()
        
        #if user:
        #    return render(request, "core/pages/permisson.html")
        #else:
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        person = Person.objects.create(endereco = endereco, user = user)
        person.save()
        return render(request, "home.html")






    
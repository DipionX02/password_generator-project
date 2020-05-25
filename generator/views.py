from django.shortcuts import render
from django.http import HttpResponse

import random #Importando todos os módulos do Random

# Create your views here.

def about(request):
    return render(request, 'generator/about.html')

def home(request):
    return render(request, 'generator/home.html')
    
def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()_.,?'))
    
    length = int(request.GET.get('length',12))

    thepassword = ''
    if length > 64:
        return render(request, 'generator/password.html',{'password':'O tamanho da senha não é suportado. Favor inserir um valor menor.'})
    else:
        for x in range(length):
            thepassword += random.choice(characters)
        return render(request, 'generator/password.html',{'password':thepassword})

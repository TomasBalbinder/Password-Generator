from hashlib import blake2b
from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.



def home(request):
    return render(request, 'generator_app/home.html')

def about(request):
    return render(request, 'generator_app/about.html')

def password(request):
    
    characters = list('abcdefghijklmnopqrstuvwxyz')

    lenght = int(request.GET.get('lenght', 5))

    thepassword = ''
    
    upper = request.GET.get('uppercase')
    if upper:
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    if request.GET.get('special characters'):
        characters.extend(list('@=!~#$%^*()-_'))
 
    
    for x in range(lenght):
        thepassword = thepassword  + random.choice(characters)
     

    
    return render(request, 'generator_app/password.html', {'password' : thepassword,'lenght': lenght, 'upper': upper})

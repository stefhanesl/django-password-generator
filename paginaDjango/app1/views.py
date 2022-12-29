from django.shortcuts import render
#from django.http import HttpResponse
import random

# Create your views here.
def about(request):
    #return HttpResponse('Hello world')
    return render(request, 'about.html')

def home(request):
    return render(request, 'home.html')


def password(request):

    caracteres = list('abcdefghijklmnopqrstuvwxyz')
    clave_generada = ''

    numero_contrasenia = int(request.GET.get('length'))

    if request.GET.get('mayuscula'):
        caracteres.extend(list('abcdefghijklmnopqrstuvwxyz'.upper()))

    if request.GET.get('numeros'):
        caracteres.extend(list('1234567890'.upper()))


    if request.GET.get('caracteres_especiales'):
        caracteres.extend(list('.,-*+/%$&()@#'.upper()))


    for elemento in range(numero_contrasenia):
        clave_generada += random.choice(caracteres)


    return render(request, 'password.html', {'password': clave_generada})
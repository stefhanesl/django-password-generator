from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
def about(request):
    #return HttpResponse('Hello world')
    return render(request, 'about.html')

def home(request):
    return render(request, 'home.html')


def password(request):
    return render(request, 'password.html')
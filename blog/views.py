from django.shortcuts import render
from django.shortcuts import HttpResponse

def about(request):
    return render(request, 'about.html')

def home(request):
    #return HttpResponse('home Page...')
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html')

def services(request):
    return render(request, 'services.html')
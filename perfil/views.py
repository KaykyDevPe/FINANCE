from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def gerenciar(request):
    return render(request, 'gerenciar.html')
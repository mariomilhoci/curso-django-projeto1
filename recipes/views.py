from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'recipes/home.html', context={'name': 'Mário César Milhoci'})


def sobre(request):
    return render(request, 'me-apague/temp.html')


def contato(request):
    return HttpResponse('CONTATO')

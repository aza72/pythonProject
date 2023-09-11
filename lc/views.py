from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index (request):
    return HttpResponse('Страница личного кабинета')

def mainpage (request):
    return HttpResponse('<H1>Главная страница </h1> ')
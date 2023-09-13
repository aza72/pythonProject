from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index (request):
    return HttpResponse('Страница личного кабинета')

def mainpage (request):
    return HttpResponse('<H1>Главная страница </h1> ')

def cat (request,catid):
    return HttpResponse('<H1>Категории </h1> ')

def archive (request,year):
    return HttpResponse(f'<H1>Архив по годам </h1><p>{year}</p> ')
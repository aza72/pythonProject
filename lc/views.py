from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
# Create your views here.
def index (request):
    return render(request,'index.html',{'title':'Главная страница'})

def about (request):
    return render(request,'lc/about.html',{'title':'Страница о нас'})

def mainpage (request):
    return HttpResponse('<H1>Глав </h1> ')

def cat (request,catid):
    if(request.GET):
        print(request.GET)
    return HttpResponse('<H1>Категории </h1> ')

def archive (request,year):
    if int (year) >2020:
        #raise Http404()
        return redirect ('home', permanent=True)
    return HttpResponse(f"<H1>Архив по годам </h1><p>{year}</p>")

def meg (request):
    return HttpResponse('<H1>Meg </h1> ')

def pageNotfount (request,exception):
    return HttpResponseNotFound('<H1>Такой страницы не существует </h1> ')
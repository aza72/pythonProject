from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *
# Create your views here.

menu =[{'title': 'О сайте', 'url_name': 'about'},
       {'title':'Добавить статью','url_name': 'add_page'},
       {'title':'Обратная связь', 'url_name': 'contact'},
       {'title':'Войти','url_name': 'login'}
       ]
def index (request):
    posts= users.objects.all()
    index_param={'posts':posts,
                 'menu':menu,
                 'title': 'Главная страница'
                 }
    return render(request, 'lc/index.html', context=index_param )

def about (request):
    return render(request,'lc/about.html',{'menu':menu,'title':'Страница о нас'})

def add_page (request):
    addpage_param = {'menu': menu,
                     'title': 'Добавить статью'
                    }
    return render(request, 'lc/addpage.html', context=addpage_param )
def contact (request):
    contact_param = {'menu': menu,
                     'title': 'Контакты'
                    }
    return render(request, 'lc/contact.html', context=contact_param )
def login (request):
    login_param = {'menu': menu,
                   'title': 'Регистрация'
                  }
    return render(request,'lc/login.html', context=login_param )




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
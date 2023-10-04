from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .forms import *
from .models import *
# Create your views here.

menu =[{'title': 'О сайте', 'url_name': 'about'},
       {'title':'Добавить статью','url_name': 'add_page'},
       {'title':'Обратная связь', 'url_name': 'contact'},
       {'title':'Войти','url_name': 'login'}
       ]

class lcHome(ListView):
    model = users
    template_name = 'lc/index.html'
    context_object_name = 'posts'
    # extra_context = {'title':'Главная страница'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Главная страница'
        context['cat_selected'] = 0
        return context

    def get_queryset(self):
        return users.objects.filter(is_published=True)


# def index (request):
#     posts= users.objects.filter(is_published=True)
#
#     index_param={'posts':posts,
#                  'menu':menu,
#                  'title': 'Главная страница',
#
#                  'cat_selected':0
#                  }
#     return render(request, 'lc/index.html', context=index_param )

def about (request):
    return render(request,'lc/about.html',{'menu':menu,'title':'Страница о нас'})

class add_page(CreateView):
    form_class = AddPostForm
    template_name = 'lc/addpage.html'
    success_url = reverse_lazy('home')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Добавление статьи'
        #context['cat_selected'] = 0
        return context

# def add_page (request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#
#                 form.save()
#                 return redirect('home')
#
#     else:
#         form = AddPostForm
#     addpage_param = {'menu': menu,
#                      'title': 'Добавить статью',
#                      'form':form
#                     }
#     return render(request, 'lc/addpage.html', context=addpage_param )
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

class showpost(DetailView):
    model = users
    template_name = 'lc/showpost.html'
    slug_url_kwarg = 'postslug'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = context['posts']
        #context['cat_selected'] = 0
        return context


# def showpost (request, postslug):
#     posts = get_object_or_404(users,slug=postslug)
#
#
#     showpost_param = {'menu': menu,
#                       'posts': posts,
#
#                       'title': posts.title,
#                       'content':posts.content,
#                       'cat_selected':posts.cat_id
#                      }
#     return render(request,'lc/showpost.html',context=showpost_param)


class lcCategory(ListView):
    model = users
    template_name = 'lc/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] ='Категория - '+ str(context['posts'][0].cat)
        context['cat_selected'] = context['posts'][0].cat_id
        return context

    def get_queryset(self):
        return users.objects.filter(cat__slug=self.kwargs['catslug'], is_published=True)

# def showcat (request, catslug):
#
#     cat = Category.objects.filter(slug=catslug)
#     posts = users.objects.filter(cat_id=cat[0].id, is_published=True)
#     for p in cat:
#         title=p.name
#         id=p.id
#
#     showcat_param = {'posts':posts,
#                      'menu':menu,
#                      'title':title,
#                      'cat_selected':id
#                      }
#     return render(request,'lc/index.html',context=showcat_param)



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
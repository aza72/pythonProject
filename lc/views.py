from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *
from .models import *
from .utils import *
# Create your views here.



class lcHome(DataMixin, ListView):

    model = users
    template_name = 'lc/index.html'
    context_object_name = 'posts'
    # extra_context = {'title':'Главная страница'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def=self.get_user_context(title='Главная страница')
        return context | c_def

    def get_queryset(self):
        return users.objects.filter(is_published=True).select_related('cat')


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
    contact_list = users.objects.all()
    paginator = Paginator(contact_list, 3)  # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'lc/about.html',{'page_obj':page_obj,'menu':menu,'title':'Страница о нас'})

class add_page(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'lc/addpage.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')
    raise_exception = True
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавление статьи')

        return context | c_def

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
# def contact (request):
#     contact_param = {'menu': menu,
#                      'title': 'Контакты'
#                     }
#     return render(request, 'lc/contact.html', context=contact_param )

class ContactFormView(DataMixin,FormView):
    form_class = ContactForm
    template_name = 'lc/contact.html'
    success_url = 'home'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Обратная связь')

        return context | c_def

    def form_valid(self,form):
        print(form.cleaned_data)
        return redirect('home')

def success (request):
    login_param = {'menu': menu,
                   'title': 'Регистрация'
                  }
    return render(request, 'lc/success.html', context=login_param)

class showpost(DataMixin, DetailView):
    model = users
    template_name = 'lc/showpost.html'
    slug_url_kwarg = 'postslug'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=['Posts'])

        return context | c_def


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


class lcCategory(DataMixin, ListView):

    model = users
    template_name = 'lc/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c = Category.objects.get(slug=self.kwargs['catslug'])
        c_def = self.get_user_context(title='Категория - '+ str(c.name),
                                      cat_selected=c.pk)
        return context | c_def

    def get_queryset(self):
        return users.objects.filter(cat__slug=self.kwargs['catslug'], is_published=True).select_related('cat')

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





class RegisterUser(DataMixin,CreateView):

    form_class = RegisterUserForm
    template_name = 'lc/register.html'
    success_url = reverse_lazy('success')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')

        return context | c_def

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin,LoginView):
    form_class = LoginUserForm
    template_name = 'lc/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')

        return context | c_def

    def get_success_url(self):
        return reverse_lazy('home')

def logout_user (request):
    logout(request)
    return redirect('login')


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
from django.urls import path, re_path
from .views import *
urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('lc/', include('lc.urls')),
    #path('lc/', index),
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('add_page/', add_page, name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('showpost/<slug:postslug>/', showpost, name='showpost'),
    path('showcat/<slug:catslug>/', showcat, name='showcat')

    #path('cat/<int:catid>/', cat),
    #re_path(r'^archive/(?P<year>[0-9]{4})/', archive),
    #path('meg', meg),
    #path('index', index),
    #
]
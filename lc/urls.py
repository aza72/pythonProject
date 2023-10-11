from django.urls import path, re_path
from django.views.decorators.cache import cache_page
from .views import *





urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('lc/', include('lc.urls')),
    #path('lc/', index),
    path('', lcHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('add_page/', add_page.as_view(), name='add_page'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('success/', success, name='success'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('showpost/<slug:postslug>/', showpost.as_view(), name='showpost'),
    path('showcat/<slug:catslug>/', lcCategory.as_view(), name='showcat')

    #path('cat/<int:catid>/', cat),
    #re_path(r'^archive/(?P<year>[0-9]{4})/', archive),
    #path('meg', meg),
    #path('index', index),
    #
]
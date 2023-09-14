from django.urls import path, re_path
from .views import *
urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('lc/', include('lc.urls')),
    #path('lc/', index),
    path('', index, name='home'),
    path('about/', about, name='about')



    #path('cat/<int:catid>/', cat),
    #re_path(r'^archive/(?P<year>[0-9]{4})/', archive),
    #path('meg', meg),
    #path('index', index),
    #
]
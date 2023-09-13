from django.urls import path,include,re_path
from .views import *
urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('lc/', include('lc.urls')),
    #path('lc/', index),
    path('', index),
    path('cat/<int:catid>/', cat),
    re_path(r'^ archive/(?P<year>[0-9]{4})/', archive),
    #path('index', index),
    #
]
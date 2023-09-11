from django.urls import path,include
from .views import *
urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('lc/', include('lc.urls')),
    #path('lc/', index),
    path('', index),
]
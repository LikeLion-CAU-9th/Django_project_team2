from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('', intro, name="intro"),
    path('home/', home, name="home"),
    path('admin/', admin.site.urls),
    path('jeongho/', include('jeongho.urls')),
    path('junho/', include('junho.urls')),
]

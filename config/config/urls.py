from django.contrib import admin
from django.urls import path, include
from .views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', intro, name="intro"),
    path('home/', home, name="home"),
    path('admin/', admin.site.urls),
    path('jeongho/', include('jeongho.urls')),
    path('junho/', include('junho.urls')),
    path('minji/', include('minji.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('', jeongho_home, name = 'jeongho_home'),
    path('room2/', room2, name = 'room2'),
]

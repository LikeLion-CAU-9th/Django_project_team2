from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'jeongho'

urlpatterns = [
    path('', jeongho_home, name = 'jeongho_home'),
]

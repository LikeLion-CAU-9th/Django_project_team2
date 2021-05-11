from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('room3/', room3, name = 'room3'),
]
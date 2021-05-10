from django.contrib import admin
from django.urls import path
import junho.views

urlpatterns = [
    path('main/', junho.views.mainpage, name = 'mainpage'),
]

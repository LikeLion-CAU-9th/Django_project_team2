from django.contrib import admin
from django.urls import path
import junho.views

urlpatterns = [
    path('room1/', junho.views.room1, name = 'room1'),
    path('room2/', junho.views.room2, name = 'room2'),
    path('room3/', junho.views.room3, name = 'room3'),
]

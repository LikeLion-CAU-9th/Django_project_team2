from django.contrib import admin
from django.urls import path
import junho.views

urlpatterns = [
    path('room1/', junho.views.room1, name = 'room1'),
]

from django.shortcuts import render

# Create your views here.

def room1(request):
    return render(request, 'room1.html')

def room2(request):
    return render(request, 'room2.html')

def room3(request):
    return render(request, 'room3.html')
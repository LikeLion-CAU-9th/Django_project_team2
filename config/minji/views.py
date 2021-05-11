from django.shortcuts import render

# Create your views here.

def room3(request):
    return render(request, template_name='room3.html')
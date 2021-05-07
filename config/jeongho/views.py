from django.shortcuts import render

def jeongho_home(request):
    return render(request, template_name='jeongho/jeongho_home.html')
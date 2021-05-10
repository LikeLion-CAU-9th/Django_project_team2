from django.shortcuts import render

def intro(request):
    intro_video = request
    return render(request, 'intro.html')
    
def home(request):
    return render(request, template_name='home.html')
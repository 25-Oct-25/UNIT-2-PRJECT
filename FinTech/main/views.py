from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse


# Create your views here.

def toggle_mode(request, mode):
    referer_url = request.META.get('HTTP_REFERER', reverse('main:home'))
    
    response = redirect(referer_url)
    
    response.set_cookie('mode', mode, max_age=365*24*60*60) 
    
    return response

def home(request):
    mode = request.COOKIES.get('mode', 'dark') 
    context = {'mode': mode}
    return render(request, 'main/home.html', context)


def history(request):
    mode = request.COOKIES.get('mode', 'dark') 
    context = {'mode': mode}
    return render(request, 'main/history.html', context)

def ecosystem(request):
    mode = request.COOKIES.get('mode', 'dark') 
    context = {'mode': mode}
    return render(request, 'main/ecosystem.html', context)

def vision(request):
    mode = request.COOKIES.get('mode', 'dark') 
    context = {'mode': mode}
    return render(request, 'main/fintechVision.html', context)


def future(request):
    mode = request.COOKIES.get('mode', 'dark') 
    context = {'mode': mode}
    return render(request, 'main/future.html', context)


def news(request):
    mode = request.COOKIES.get('mode', 'dark') 
    context = {'mode': mode}
    return render(request, 'main/news.html', context)


def regulations(request):
    mode = request.COOKIES.get('mode', 'dark') 
    context = {'mode': mode}
    return render(request, 'main/regulation.html', context)
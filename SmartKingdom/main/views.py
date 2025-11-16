from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest ######
#create your views here.


def home(request: HttpRequest):
    response = render(request, "main/home.html", {'page_name': 'home'})
    response.set_cookie("name", "value")
    return response

def jeddah(request: HttpRequest):
    return render(request, "main/Jeddah.html", {'page_name': 'jeddah'})

def neom(request: HttpRequest):
    return render(request, "main/Neom.html", {'page_name': 'neom'})

def qiddiya(request: HttpRequest):
    return render(request, "main/Qiddiya.html", {'page_name': 'qiddiya'})

def spark(request: HttpRequest):
    return render(request, "main/Spark.html", {'page_name': 'spark'})

def the_line(request: HttpRequest):
    return render(request, "main/Theline.html", {'page_name': 'the_line'})

def riyadh(request: HttpRequest):
    return render(request, "main/Riyadh.html", {'page_name': 'riyadh'})

def toggle_dark_mode(request: HttpRequest):

    current_mode = request.COOKIES.get('dark_mode', 'light')
    
    if current_mode == 'light':
        new_mode = 'dark'
    else:
        new_mode = 'light'
    
    previous_page = request.META.get('HTTP_REFERER', '/')
    response = redirect(previous_page)
    
    response.set_cookie('dark_mode', new_mode, max_age=365*24*60*60)
    
    return response
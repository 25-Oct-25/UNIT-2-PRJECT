from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
# Create your views here.

def home_page(request : HttpRequest):
    return render(request, "main/home_page.html")

def about(request : HttpRequest):
    return render(request, "main/about.html")

def tourism(request : HttpRequest):
    return render(request, "main/tourism.html")

def redsea_global(request : HttpRequest):
    return render(request, "main/redsea_global.html")

def amaala(request : HttpRequest):
    return render(request, "main/amaala.html")

def alula(request : HttpRequest):
    return render(request, "main/alula.html")

def sindalah(request : HttpRequest):
    return render(request, "main/sindalah.html")

def deseret_rock(request : HttpRequest):
    return render(request, "main/deseret_rock.html")

def programs(request : HttpRequest):
    return render(request, "main/programs.html")



def light_mode(request : HttpRequest):
    response = redirect("main:home_page")
    response.set_cookie("mode", "light", max_age=60*60)
    return response

def dark_mode(request : HttpRequest):
    response = redirect("main:home_page")
    response.set_cookie("mode", "dark", max_age=60*60)
    return response

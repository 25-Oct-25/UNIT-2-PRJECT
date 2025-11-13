from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

# Create your views here.

def home_view(request: HttpRequest):
    return render(request, "main/home.html")

def about_view(request:HttpRequest):
    return render(request,"main/about.html")

def education_view(request:HttpRequest):
    return render(request,"main/education.html")

def science_view(request:HttpRequest):
    return render(request,"main/science.html")

def sports_view(request:HttpRequest):
    return render(request,"main/sports.html")

def esports_view(request:HttpRequest):
    return render(request,"main/esports.html")

def art_view(request:HttpRequest):
    return render(request,"main/art.html")

def mode_view(request:HttpRequest, mode):
    
    response = redirect(request.GET.get("page",'/'))

    if mode == "dark":
        response.set_cookie("mode", "dark", max_age=60*60*24*7)
    elif mode == "light":
        response.set_cookie("mode", "dark", max_age=-3600)

    return response
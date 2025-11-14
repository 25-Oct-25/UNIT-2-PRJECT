from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.

def home_page(request:HttpRequest):
    return render(request, "SaudiaArabia/home.html")

def history_page(request:HttpRequest):
    return render(request, "SaudiaArabia/history.html")

def tourism_page(request:HttpRequest):
    return render(request, "SaudiaArabia/tourism.html")

def culture_page(request:HttpRequest):
    return render(request, "SaudiaArabia/culture.html")

def manufacturing_page(request:HttpRequest):
    return render(request, "SaudiaArabia/manufacturing.html")

def vision_page(request:HttpRequest):
    return render(request, "SaudiaArabia/vision.html")

def education_page(request:HttpRequest):
    return render(request, "SaudiaArabia/education.html")
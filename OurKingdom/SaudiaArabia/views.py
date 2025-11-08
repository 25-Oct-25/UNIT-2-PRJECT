from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_page(request):
    return HttpResponse("home page")

def history_page(request):
    return HttpResponse("history page")

def tourism_page(request):
    return HttpResponse("tourism page")

def culture_page(request):
    return HttpResponse("culture page")

def manufacturing_page(request):
    return HttpResponse("manufacturing page")

def vision_page(request):
    return HttpResponse("vision page")

def education_page(request):
    return HttpResponse("education page")

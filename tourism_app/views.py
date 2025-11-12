from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def index_view(request:HttpRequest):
    return render(request, "tourism_app/index.html")

def discover_food(request):
    return render(request, 'tourism_app/discover-food.html')

def discover_season(request):
    return render(request, 'tourism_app/discover-season.html')

def discover_planning(request):
    return render(request, 'tourism_app/discover-planning.html')

def places_jeddah(request):
    return render(request, 'tourism_app/places-jeddah.html')

def places_riyadh(request):
    return render(request, 'tourism_app/places-riyadh.html')

def places_alula(request):
    return render(request, 'tourism_app/places-alula.html')


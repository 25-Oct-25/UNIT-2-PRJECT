from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

#Home page
def home_view(request : HttpRequest):

    return render( request, "main/home.html")

#Future page
def future_view(request : HttpRequest):

    return render( request, "main/future.html")

#المبادرات
def initiatives_view(request : HttpRequest):

    return render( request, "main/initiatives.html")

#Creative page
def innovation_view(request : HttpRequest):

    return render( request, "main/innovation.html")

#Impact page
def impact_view(request : HttpRequest):

    return render( request, "main/impact.html")

#Fields page
def fields_view(request : HttpRequest):

    return render( request, "main/fields.html")
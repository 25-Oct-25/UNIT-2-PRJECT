from django.urls import path
from . import views

app_name = "main"

urlpatterns= [
    path("",views.home_view, name= "home_view"),
    path("about/", views.about_view, name="about_view"),
    path("education/", views.education_view, name="education_view"),
    path("science/", views.science_view, name="science_view"),
    path("sports/", views.sports_view, name="sports_view"),
    path("esports/", views.esports_view, name="esports_view"),
    path("art/", views.art_view, name="art_view"),
    path("mode/<mode>/", views.mode_view, name="mode_view"),
]
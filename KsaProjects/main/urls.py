from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.home_page, name="home_page"),
    path("about/", views.about, name="about"),
    path("tourism/", views.tourism, name="tourism"),
    path("redsea_global/", views.redsea_global, name="redsea_global"),
    path("amaala/", views.amaala, name="amaala"),
    path("alula/", views.alula, name="alula"),
    path("sindalah/", views.sindalah, name="sindalah"),
    path("deseret_rock/", views.deseret_rock, name="deseret_rock"),
    path("programs/", views.programs, name="programs"),

    path("light/mode/", views.light_mode, name="light_mode"),
    path("dark/mode/", views.dark_mode, name="dark_mode"),
]
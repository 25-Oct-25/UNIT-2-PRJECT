from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("destinations/<slug:slug>/", views.city_detail, name="city_detail"),
    path("saudi-calendar/", views.all_events_page, name="all_events"),
    path("saudi-map/", views.saudi_map_page, name="saudi_map"),
    path("toggle-theme/", views.toggle_theme, name="toggle_theme")
]
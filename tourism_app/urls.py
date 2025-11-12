from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index_view'),
    # Discover pages
    path('discover-food/', views.discover_food, name='discover_food'),
    path('discover-season/', views.discover_season, name='discover_season'),
    path('discover-planning/', views.discover_planning, name='discover_planning'),

    # Places pages
    path('places-jeddah/', views.places_jeddah, name='places_jeddah'),
    path('places-riyadh/', views.places_riyadh, name='places_riyadh'),
    path('places-alula/', views.places_alula, name='places_alula'),
]
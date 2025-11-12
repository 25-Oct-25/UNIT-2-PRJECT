from django.urls import path,include
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('history/', views.history, name='history'),
    path('ecosystem/', views.ecosystem, name='ecosystem'),
    path('vision/', views.vision, name='vision'),
    path('future/', views.future, name='future'),
    path('news/', views.news, name='news'),
    path('regulations/', views.regulations, name='regulation'),
    path('toggle_mode/<str:mode>/', views.toggle_mode, name='toggle_mode'),
]

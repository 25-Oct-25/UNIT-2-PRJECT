from django.urls import path
from . import views

app_name = 'main'

urlpatterns =[
    path('', views.home_view, name='home'),
    path('period/<slug:slug>/', views.period_view, name='period_detail'),
    path("theme/toggle/", views.toggle_theme, name="toggle_theme"),
]
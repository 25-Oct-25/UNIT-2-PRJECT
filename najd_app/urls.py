from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('riyadh/', views.riyadh, name='riyadh'),
    path('diriyah/', views.diriyah, name='diriyah'),
    path('dhurma/', views.dhurma, name='dhurma'),
    path('marat/', views.marat, name='marat'),
    path('shaqra/', views.shaqra, name='shaqra'),
    path('neom/', views.neom, name='neom'),
    path('contact/', views.contact, name='contact'),
]
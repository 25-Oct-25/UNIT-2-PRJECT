from django.urls import path
from . import views

# مهم جداً لاستخدام reverse lookups مثل redirect('main:contact')
app_name = "main" 

urlpatterns = [
    # الصفحات الرئيسية
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    
    # صفحة التواصل (التي تعالج الآن النموذج في views.py)
    path('contact/', views.contact, name='contact'),
    
    # صفحات المدن
    path('riyadh/', views.riyadh, name='riyadh'),
    path('jeddah/', views.jeddah, name='jeddah'),
    path('alula/', views.alula, name='alula'),
    path('abha/', views.abha, name='abha'),
    path('khobar/', views.khobar, name='khobar'),
    path('tabuk/', views.tabuk, name='tabuk'),
    path('activities/', views.activities, name='activities'),
]
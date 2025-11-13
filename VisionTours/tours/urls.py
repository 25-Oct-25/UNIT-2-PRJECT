from . import views
from django.urls import path

app_name = 'tours'


urlpatterns = [
    path('', views.home_view, name='home'),
    path('project/neom/', views.neom_view, name='neom'),
    path('project/redsea/', views.redsea_view, name='redsea'),
    path('project/qiddiya/', views.qiddiya_view, name='qiddiya'),
    path('project/diriyah/', views.diriyah_view, name='diriyah'),
    path('project/mukaab/', views.mukaab_view, name='mukaab'),
    path('progress-map/', views.progress_map_view, name='progress_map'),
    path('toggle-theme/', views.toggle_theme, name='toggle_theme'),
]
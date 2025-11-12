from . import views
from django.urls import path
# اسم معرف التطبيق
app_name="main"
# روابط الصفحات : المسارات ومعرفاتها عشان يسهل اسويه داينمك بعدين بمعرف التطبيق و  معرف المسار
urlpatterns = [
    path("", views.home_view, name="home_view"), 
    path("health/", views.health_view, name="health_view"),
    path("education/", views.education_view, name="education_view"),
    path("economy/", views.economy_view, name="economy_view"),
    path("technology/", views.technology_view, name="technology_view"),
    path("vision/", views.vision_view, name="vision_view"), # Vision 2030
    path("about/", views.about_view, name="about_view"), # About Saudi Arabia
    path("film/", views.film_view, name="film_view"),
    path("contact/", views.contact_view, name="contact_view"),   
    path("theme/<str:mode>/", views.set_theme_view, name="set_theme_view"), # هذا المسار للتحويل بين الدارك مود والعادي 
         
]

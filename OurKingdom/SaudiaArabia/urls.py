from django.urls import path
from . import views

app_name = "OurKingdom"
urlpatterns = [
    path("",               views.home_page,          name="home_page"         ),
    path("vision/",        views.vision_page,        name="vision_page"       ),
    path("history/",       views.history_page,       name="history_page"      ),
    path("tourism/",       views.tourism_page,       name="tourism_page"      ),
    path("culture/",       views.culture_page,       name="culture_page"      ),
    path("education/",     views.education_page,     name="education_page"    ),
    path("manufacturing/", views.manufacturing_page, name="manufacturing_page"), 
]
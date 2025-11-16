from . import views # هنا نستورد ملف views من نفس المجلد الحالي
from django.urls import path # هنا نستورد دالة path لتحديد مسارات URL
 

app_name = "main" # تعريف اسم التطبيق لتجنب التعارض في أسماء المسارات

urlpatterns = [# هنا نحدد قائمة المسارات
    path("", views.home, name="home"),  # الصفحة الرئيسية - المسار الفارغ
    path("home/", views.home, name="home_alt"),  # مسار بديل للصفحة الرئيسية
    path("home/jeddah/", views.jeddah, name="jeddah"),
    path("home/neom/", views.neom, name="neom"),
    path("home/qiddiya/", views.qiddiya, name="qiddiya"),
    path("home/riyadh/", views.riyadh, name="riyadh"),
    path("home/spark/", views.spark, name="spark"),
    path("home/the_line/", views.the_line, name="the_line"),
    path("toggle-dark-mode/", views.toggle_dark_mode, name="toggle_dark_mode"),
]
"""
URL configuration for DiscoverSaudiArabia project.
"""

from django.contrib import admin
from django.urls import path, include
# 👇 يجب استيراد الإعدادات وتابع الـ static
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',include("main.urls")),
]

# 🌟🌟🌟 الخطوة النهائية: إضافة مسار الـ Static في وضع التطوير 🌟🌟🌟
# هذا يضمن أن يتم تحميل ملفات الـ CSS والـ JS، والتي بدونها قد تفشل الصفحة في التحميل
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # لا تقلقي من STATIC_ROOT، لقد تم إعداده بشكل صحيح في settings.py
    
# بما أنك تستخدمين Python 3.13، قد تحتاجين أيضًا لتحديد Media URL إذا كان لديك صور مرفوعة
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
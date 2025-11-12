from django.shortcuts import render, redirect 
from django.core.mail import send_mail 
from django.conf import settings
from django.contrib import messages

# الدوال الحالية لديكِ (الاستدعاء المجرد)
def home(request):
    return render(request, 'home.html') # 🌟 تم التعديل

def about(request):
    return render(request, 'about.html') # 🌟 تم التعديل

# دالة معالجة صفحة التواصل (Contact) 
def contact(request):
    # 1. معالجة طلب إرسال النموذج (POST)
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        full_message = f"الرسالة من: {name}\nالبريد الإلكتروني: {email}\n\n{message}"
        
        try:
            send_mail(
                subject, 
                full_message, 
                settings.DEFAULT_FROM_EMAIL, 
                [settings.RECIPIENT_ADDRESS], 
                fail_silently=False,
            )
            messages.success(request, 'تم استلام رسالتك بنجاح! شكراً لك.')
        except Exception as e:
            print(f"Error sending email: {e}")
            messages.error(request, 'عفواً، حدث خطأ أثناء إرسال الرسالة. يرجى المحاولة لاحقاً.')
        
        return redirect('contact') 

    # 2. عرض القالب عند طلب الصفحة (GET)
    return render(request, 'contact.html') # 🌟 تم التعديل

# الدوال الخاصة بالمدن
def riyadh(request):
    return render(request, 'riyadh.html')

def jeddah(request):
    return render(request, 'jeddah.html')

def alula(request):
    return render(request, 'alula.html')

def abha(request):
    return render(request, 'abha.html')

def khobar(request):
    return render(request, 'khobar.html')

def tabuk(request):
    return render(request, 'tabuk.html')

def activities(request):
    return render(request, 'activities.html')
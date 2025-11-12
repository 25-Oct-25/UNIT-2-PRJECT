from django.http import HttpRequest
from django.shortcuts import render, redirect


# الصفحات الرئيسية

def home_view(request: HttpRequest):
    cards = [
        {
            "url_name": "main:health_view",
            "name": "Health",
            "desc": "Stronger systems, faster response, smarter services.",
            "bg": "static/images/health.jpg",
        },
        {
            "url_name": "main:education_view",
            "name": "Education",
            "desc": "Learning never stopped thanks to Allah then national platforms.",
            "bg": "static/images/education.jpg",
        },
        {
            "url_name": "main:economy_view",
            "name": "Economy",
            "desc": "Stability measures and SME support accelerated growth.",
            "bg": "static/images/economy.jpg",
        },
        {
            "url_name": "main:technology_view",
            "name": "Technology",
            "desc": "Seamless services powered by data and AI.",
            "bg": "static/images/technology.jpg",
        },
    ]
    return render(request, "main/home.html", {"cards": cards}) # اخر خانه هنا لتمرير البيانات


def health_view(request: HttpRequest):
    return render(request, "main/health.html")


def education_view(request: HttpRequest):
    return render(request, "main/education.html")


def economy_view(request: HttpRequest):
    return render(request, "main/economy.html")


def technology_view(request: HttpRequest):
    return render(request, "main/technology.html")


def vision_view(request: HttpRequest):
    return render(request, "main/vision.html")


def about_view(request: HttpRequest):
    return render(request, "main/about.html")


def film_view(request: HttpRequest):
    return render(request, "main/film.html")


def contact_view(request: HttpRequest):
    ctx = {"sent": False}

    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        topic = request.POST.get("topic", "").strip()
        message = request.POST.get("message", "").strip()

        # هنا لو كان فيه مسج يخلي السنت ترو عشان بالتامبلت اخلي رساله النجاح تظهر
        if message: 
            ctx.update({
                "sent": True,
                "name": name,
                "email": email,
                "topic": topic,
                "message": message,
            })
    # هنا نفس الحكايه مررت بيانات اذاالرسالة قيمتها فولس بتعرض النموذج اذا ترو تعرض النموذج ورساله النجاح
    return render(request, "main/contact.html", ctx)



# هذي الداله للتحويل بين الدارك مود و العادي و الكوكيز الي هنا خليتها سنه  
def set_theme_view(request: HttpRequest, mode: str):
    mode = (mode or "").lower()
    if mode not in ("light", "dark"):
        return redirect(request.META.get("HTTP_REFERER", "/"))

    resp = redirect(request.META.get("HTTP_REFERER", "/"))
    resp.set_cookie("theme", mode, max_age=60 * 60 * 24 * 365) #سنه
    return resp
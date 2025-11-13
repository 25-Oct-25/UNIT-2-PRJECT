from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect


def _theme_from_request(request):
    return request.COOKIES.get("theme", "light")

def home_view(request):
    theme = _theme_from_request(request)

    return render(request, "main/home.html",{"theme":'light'})


def period_view(request, slug):
    templates = {
        "first-saudi-state": "main/periods/first-saudi-state.html",
        "second-saudi-state": "main/periods/second-saudi-state.html",
        "third-saudi-state": "main/periods/third-saudi-state.html",
        "unification": "main/periods/unification-1932.html",
        "development-era": "main/periods/development-era.html",
        "vision-2030": "main/periods/vision-2030.html",
    }

    if slug not in templates:
        raise Http404("الفترة غير موجودة")
    theme = _theme_from_request(request)
    return render(request, templates[slug],{"theme":'light'})


def toggle_theme(request):
    current = request.COOKIES.get("theme" "light")
    new_theme = "dark" if current != "dark" else "light"

    resp = HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))
    resp.set_cookie(
        "theme",
        new_theme,
        max_age=60 * 60 * 24 * 90,  
        httponly=False,             
        samesite="Lax",
    )
    return resp



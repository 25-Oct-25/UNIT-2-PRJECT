from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse 
from django.shortcuts import resolve_url
from django.shortcuts import redirect


def index_view(request: HttpRequest):
    font_size = request.COOKIES.get('font_size', 'normal')
    return render(request, "main/index.html", {'font_size': font_size})


def heritage_view(request: HttpRequest):
    return render(request, "main/heritage.html")


def art_view(request: HttpRequest):
    return render(request, "main/art.html")


def architecture_view(request: HttpRequest):
    return render(request, "main/architecture.html")


def festivals_view(request: HttpRequest):
    return render(request, "main/festivals.html")


def fashion_view(request: HttpRequest):
    return render(request, "main/fashion.html")


def music_view(request: HttpRequest):
    return render(request, "main/music.html")


# cookies view for font
def toggle_font(request):
    current_size = request.COOKIES.get('font_size', 'normal')

    if current_size == 'normal':
        new_size = 'large'
    else:
        new_size = 'normal'
    response = JsonResponse({'status': 'success', 'font_size': new_size})
    response.set_cookie('font_size', new_size)

    return response
from django.shortcuts import render

def index(request):
    context = {
        'title': 'Where Heritage Meets the Horizon',
    }
    return render(request, 'index.html', context)

def riyadh(request):
    return render(request, 'riyadh.html')

def diriyah(request):
    return render(request, 'diriyah.html')

def dhurma(request):
    return render(request, 'dhurma.html')

def marat(request):
    return render(request, 'marat.html')

def shaqra(request):
    return render(request, 'shaqra.html')

def neom(request):
    return render(request, 'neom.html')

def contact(request):
    return render(request, 'contact.html')
from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse

# ================================================
# 1. Database مؤقته
# ================================================

# CITIES 
# (تركت هذا القسم كما هو تماماً بناءً على طلبك)
CITIES = {
    "riyadh":  {
        "name": "Riyadh",  
        "slug": "riyadh", 
        "tag": "قلب المملكة النابض", 
        "cover_image": "core/img/Riyadh.jpg",
        "summary": "Steeped in heritage yet bustling with modern flair, Riyadh effortlessly blends its captivating past with a dynamic present. Explore the UNESCO listed streets of Al Turaif, where centuries-old architecture tells stories of trade."
    },
    "abha":    {
        "name": "Abha",    
        "slug": "abha",   
        "tag": "عروس الجنوب", 
        "cover_image": "core/img/ABHA3.jpg",
        "summary": "Known as the 'Bride of the Mountain', Abha is a city of stunning natural beauty, high altitudes, and a cool climate. Explore its vibrant art scene and the dense forests of Aseer National Park."
    },
    "makkah":  {
        "name": "Makkah",  
        "slug": "makkah", 
        "tag": "روح المكان", 
        "cover_image": "core/img/Makkah.jpg",
        "summary": "The spiritual heart of Islam, Makkah is a city of profound religious significance. While its core is centered on Hajj and Umrah, the surrounding region offers unique cultural and historical insights."
    },
    "alula":   {
        "name": "AlUla",   
        "slug": "alula",  
        "tag": "تاريخ ينطق بالجمال", 
        "cover_image": "core/img/ZZZ.jpg",
        "summary": "A living museum of preserved tombs, sandstone outcrops and historic dwellings. AlUla is home to Hegra, Saudi Arabia's first UNESCO World Heritage Site, and a land of breathtaking natural wonders."
    },
    "jeddah":  {
        "name": "Jeddah",  
        "slug": "jeddah", 
        "tag": "عروس البحر الأحمر", 
        "cover_image": "core/img/Jeddah.jpg",
        "summary": "A must-see historical city on the Red Sea. Jeddah effortlessly blends its captivating past with a dynamic present. Explore the UNESCO listed streets of Al Balad, where centuries-old architecture tells stories of trade and culture."
    },
}

# DESTINATIONS
# (تركت هذا القسم كما هو تماماً بناءً على طلبك)
DESTINATIONS = [
    {'id': 1, 'city_slug': 'alula', 'name': 'Half Day in AlUla Cultural', 'description': 'Discovery & Success Wondes...', 'price': 5000, 'image': 'core/img/Ad.jpeg'},
    {'id': 2, 'city_slug': 'alula', 'name': 'Hike in AlUla', 'description': 'Rock formations and visit to th...', 'price': 270, 'image': 'core/img/Hike.jpg'},
    {'id': 3, 'city_slug': 'alula', 'name': '2 Days in AlUla', 'description': 'Explore Arabian Nights with Mod...', 'price': 5000, 'image': 'core/img/arabian_nights.jpeg'},
    {'id': 4, 'city_slug': 'jeddah', 'name': 'Red Sea Diving', 'description': 'Explore the vibrant coral reefs...', 'price': 350, 'image': 'core/img/Diving.jpg'},
    {'id': 5, 'city_slug': 'riyadh', 'name': 'Edge of the World Tour', 'description': 'A day trip to the stunning cliffs...', 'price': 150, 'image': 'core/img/world.jpg'},
    {'id': 6, 'city_slug': 'abha', 'name': 'Aseer National Park Tour', 'description': 'Explore the dense forests and stunning views.', 'price': 250, 'image': 'core/img/Asir.jpg'}
    
]

# EVENTS (الفعاليات)
# (تركت هذا القسم كما هو تماماً بناءً على طلبك)
EVENTS = [
    {'id': 1, 'city_slug': 'riyadh', 'name': 'Shopping Festival', 'location_text': 'DIRIYAH | SHOPPING', 'price_text': '', 'event_date': '2025-11-09', 'image': 'core/img/Shooping.jpg'},
    {'id': 2, 'city_slug': 'jeddah', 'name': 'Concert Show', 'location_text': 'JEDDAH | CONCERT SHOW', 'price_text': 'From $ 107', 'event_date': '2025-10-29', 'image': 'core/img/Show.jpg'},
    {'id': 3, 'city_slug': 'jeddah', 'name': 'Ashtanga Vinyasa Yoga', 'location_text': 'JEDDAH | YOGA', 'price_text': 'From $ 100', 'event_date': '2025-11-21', 'image': 'core/img/yoga.jpg'},
    {'id': 4, 'city_slug': 'riyadh', 'name': 'Music Festival', 'location_text': 'RIYADH | ENTERTAINMENT', 'price_text': '', 'event_date': '2025-11-30', 'image': 'core/img/Show.jpg'},
    {'id': 5, 'city_slug': 'abha', 'name': 'Abha Arts Festival', 'location_text': 'ABHA | CULTURE', 'price_text': 'Free Entry', 'event_date': '2025-12-10', 'image': 'core/img/Abha-Art.jpg'
    }
]   

# ================================================
# 2.  (Views) 
# ================================================

def get_base_context(request):
    theme_mode = request.COOKIES.get('theme', 'dark') 
    return {
        'theme_mode': theme_mode,
        'cities': CITIES,
    }


def toggle_theme(request):
    
    current_theme = request.COOKIES.get('theme', 'dark')
    
   # revert the theme
    new_theme = "light" if current_theme == "dark" else "dark"
    
    
    redirect_url = request.META.get('HTTP_REFERER', reverse('core:home'))
    resp = HttpResponseRedirect(redirect_url)
    
   
    resp.set_cookie('theme', new_theme, max_age=60*60*24*365) 
    
    return resp



def home(request):
    context = get_base_context(request) 
    context.update({
        'adventures': DESTINATIONS[:5],
        'events': EVENTS[:5],
    })
    return render(request, "core/home.html", context)

def city_detail(request, slug):
    context = get_base_context(request) # <-- تم التعديل هنا
    city = CITIES.get(slug)
    if not city:
        raise Http404("City not found")
        
    adventures_in_city = [d for d in DESTINATIONS if d['city_slug'] == slug]
    events_in_city = [e for e in EVENTS if e['city_slug'] == slug]
    
    context.update({
        'city': city,
        'adventures': adventures_in_city,
        'events': events_in_city,
    })
    return render(request, "core/city_detail.html", context)


def about(request):
    context = get_base_context(request) # <-- تم التعديل هنا
    return render(request, "core/about.html", context)

def contact(request):
    context = get_base_context(request) # <-- تم التعديل هنا
    if request.method == "POST":
        context["sent"] = True
        return render(request, "core/contact.html", context)
    return render(request, "core/contact.html", context)

def all_events_page(request):
    context = get_base_context(request) # <-- تم التعديل هنا
    context.update({
        'events': EVENTS,
    })
    return render(request, 'core/all_events.html', context)

def saudi_map_page(request):
    context = get_base_context(request) # <-- تم التعديل هنا
    return render(request, 'core/saudi_map.html', context)
from datetime import date
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.utils.dateparse import parse_date

def _get_theme(request):
    t = request.COOKIES.get('theme', 'light')
    return 'dark' if t == 'dark' else 'light'

def _render(request, template_name, extra_context=None):
    base = {'theme': _get_theme(request)}
    if extra_context:
        base.update(extra_context)
    return render(request, template_name, base)

def toggle_theme(request):
    next_url = request.GET.get('next', '/')
    current = _get_theme(request)
    new_theme = 'light' if current == 'dark' else 'dark'
    resp = redirect(next_url)
    resp.set_cookie('theme', new_theme, max_age=60*60*24*365, samesite='Lax')
    return resp

def home_view(request):
    vision_projects = [
        {"tag": "Future City","title": "NEOM: The Line","description": "The 170 km long cognitive city is a revolutionary concept for urban living. The Line is set to host 9 million residents and run entirely on renewable energy.","image": "neom1.jpg","url_name": "tours:neom"},
        {"tag": "Regenerative Tourism","title": "The Red Sea Project","description": "A luxury coastal development focusing on environmental sustainability and regeneration. It features a stunning archipelago of over 90 islands.","image": "redsea-cover.jpg","url_name": "tours:redsea"},
        {"tag": "Entertainment Capital","title": "Qiddiya","description": "Qiddiya is positioned to become the capital of Entertainment, Sports, and Arts. It will host world-class theme parks and sporting facilities.","image": "qiddiya-cover.jpg","url_name": "tours:qiddiya"},
        {"tag": "Historical & Cultural","title": "Diriyah Gate","description": "A multi-billion dollar project to transform the historic birthplace of the Kingdom into a global hub for culture and hospitality.","image": "diriyah-cover.jpg","url_name": "tours:diriyah"},
        {"tag": "Architectural Icon","title": "The Mukaab","description": "The Mukaab will be an iconic landmark in the heart of Riyadh's New Murabba project, offering a fully immersive retail and cultural experience.","image": "mukaab-cover.jpg","url_name": "tours:mukaab"},
    ]
    return _render(request, 'tours/home.html', {'vision_projects': vision_projects})

def neom_view(request):
    return _render(request, 'tours/neom.html')

def redsea_view(request):
    return _render(request, 'tours/redsea.html')

def qiddiya_view(request):
    return render(request, 'tours/qiddiya.html', {'theme': _get_theme(request)})

def diriyah_view(request):
    return _render(request, 'tours/diriyah.html')

def mukaab_view(request):
    return _render(request, 'tours/mukaab.html')

PM_STEPS = ["Planning", "Infrastructure", "Build", "Testing", "Operations"]

PROJECTS = [
    {"slug": "diriyah","title": "Diriyah","status": "Completed","phase": "Operations","progress": 100,"updated": "2025-10-01","image": "cards/diriyah-cover.jpg","url_name": "tours:diriyah","desc": "The heritage heart of Saudi Arabia—Najdi architecture, cultural venues, restaurants, and vibrant public spaces.","step_index": 4},
    {"slug": "redsea","title": "The Red Sea Project","status": "Under Construction","phase": "Phase 2","progress": 65,"updated": "2025-09-20","image": "cards/redsea-cover.jpg","url_name": "tours:redsea","desc": "Luxury regenerative tourism across a stunning archipelago with strict environmental stewardship.","step_index": 2},
    {"slug": "neom","title": "NEOM — The Line","status": "Under Construction","phase": "Core Infrastructure","progress": 40,"updated": "2025-10-10","image": "cards/neom1.jpg","url_name": "tours:neom","desc": "A 170-km linear city for 9M residents, powered by clean energy and designed around people, not cars.","step_index": 1},
    {"slug": "qiddiya","title": "Qiddiya","status": "Under Construction","phase": "Parks & Venues","progress": 55,"updated": "2025-09-12","image": "cards/qiddiya-cover.jpg","url_name": "tours:qiddiya","desc": "The capital of Entertainment, Sports, and Arts with record-breaking rides and global venues.","step_index": 3},
    {"slug": "mukaab","title": "The Mukaab","status": "Planning","phase": "Concept Development","progress": 25,"updated": "2025-08-30","image": "cards/mukaab-cover.jpg","url_name": "tours:mukaab","desc": "An immersive mixed-use landmark in New Murabba—future retail, culture, and hospitality experiences.","step_index": 0},
]

def _pm_kpis(projects):
    total = len(projects)
    completed = sum(1 for p in projects if p["status"] == "Completed")
    ongoing = sum(1 for p in projects if p["status"] == "Under Construction")
    last_update = max((parse_date(p["updated"]) for p in projects if p.get("updated")), default=date.today())
    return {"pm_kpi_total": total,"pm_kpi_completed": completed,"pm_kpi_ongoing": ongoing,"pm_kpi_last_update": last_update.isoformat()}

def progress_map_view(request):
    ctx = {"pm_steps": PM_STEPS, "pm_projects": PROJECTS}
    ctx.update(_pm_kpis(PROJECTS))
    return _render(request, 'tours/progress-map.html', ctx)

from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, get_object_or_404, redirect
from .models import Gul,Turlar

def index(request:WSGIRequest):
    guls = Gul.objects.all()

    context = {
        "guls":guls,
        "title":"Gull savdo!"
    }
    return render(request,"index.html",context)

def gul_by_tur(request, turi_id):
    gul = get_object_or_404(Gul, pk=turi_id)
    turs = Turlar.objects.filter(turi_id=turi_id)
    context = {
        "turs": turs,
        "title": f"{gul.name}: Barcha Gullar!"
    }
    return render(request, "index.html", context)


def gul_detail(request: WSGIRequest, pk):
    guls = get_object_or_404(Gul, pk=pk)
    context = {
        "guls": guls,
        "title": guls.name
    }
    return render(request, 'detail.html', context)

from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, get_object_or_404, redirect
from .models import Gul,Turlar
from .forms import GulForm

def index(request:WSGIRequest):
    guls = Gul.objects.all()

    context = {
        "guls":guls,
        "title":"Gull savdo!"
    }
    return render(request,"index.html",context)

def gul_by_tur(request, turi_id):
    guls = Gul.objects.filter(turi_id=turi_id)
    turs = get_object_or_404(Turlar, pk=turi_id)
    context = {
        "guls": guls,
        "title": f"{turs.name}: Barcha Gullar!"
    }
    return render(request, "index.html", context)



def gul_detail(request: WSGIRequest, pk):
    guls = get_object_or_404(Gul, pk=pk)
    context = {
        "guls": guls,
        "title": guls.name
    }
    return render(request, 'detail.html', context)

def add_post(request: WSGIRequest):
    if request.method == 'POST':
        form = GulForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            post = form.create()
            return redirect('detail', pk=post.pk)
    else:
        form = GulForm()
    context = {
        "form": form
    }
    return render(request, 'add_post.html', context)

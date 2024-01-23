from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render

from .models import Kategoria, Obiekt


def index(request):
    if request.method == "POST":
        data = request.POST
        nazwa = data.get("nazwa")

        if nazwa:
            opis = data.get("opis")
            latitude = data.get("lan")
            longitude = data.get("lon")
            kategoria = data.get("kategoria")

            nowy = Obiekt(title=nazwa, opis=opis, longitude=longitude, latitude=latitude, kategoria=Kategoria.objects.get(title=kategoria))
            nowy.save()

            return HttpResponseRedirect('http://127.0.0.1:8000/mapa/')
        else:
            kategoria = data.get("kategoria")
            if kategoria != "Kategoria obiektu":
                obiekty = Obiekt.objects.all().filter(kategoria=Kategoria.objects.get(title=kategoria))
            else:
                obiekty = Obiekt.objects.all()

            kategorie = Kategoria.objects.all()
            context = {"obiekty": obiekty, "kategorie": kategorie}
            return render(request, "index.html", context)
    else:
        obiekty = Obiekt.objects.all()
        kategorie = Kategoria.objects.all()
        context = {"obiekty": obiekty, "kategorie": kategorie}
        return render(request, "index.html", context)
from django.shortcuts import render
from .models import BusStation, Line, Passengers
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms

# Create your views here.
def line_index(request):
    lines = Line.objects.all()
    context = {
        "lines": lines,
    }
    return render(request, "lines/line_index.html", context)

def line_detail(request, line_id):
    line = Line.objects.get(id=line_id)
    passengers = line.passengers.all()
    non_passengers = Passengers.objects.exclude(routes=line).all()
    
    
    context = {
        "line": line,
        "passengers": passengers,
        "non_passengers": non_passengers
    }
    return render(request, "lines/line_detail.html", context) 


def booking(request, line_id):
    if request.method == "POST":
        line = Line.objects.get(pk=line_id)
        passenger_id = int(request.POST["passenger"])
        passenger = Passengers.objects.get(pk = passenger_id)
        passenger.routes.add(line)
        return HttpResponseRedirect(reverse("line_detail", args=(line_id,)))
    

    
    


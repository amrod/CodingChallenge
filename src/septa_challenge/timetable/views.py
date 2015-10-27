from django.shortcuts import render
from django.http import HttpResponse

from . import models
from . import services

def home(request):
    stations = models.Station.objects.all().order_by('name')

    context = {'stations': stations}

    return render(request, 'main.html', context)






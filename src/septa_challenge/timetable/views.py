from django.shortcuts import render
from django.http import HttpResponse

from . import models
from . import services

def home(request):
    stations = models.Station.objects.all().order_by('name')

    context = {'stations': stations}

    if request.method == 'POST':
        start = request.POST.get('start_station')
        end = request.POST.get('end_station')
        ss = services.SEPTAServices()

        trains = ss.get_next_to_arrive(start, end)
        context['trains'] = trains

    return render(request, 'main.html', context)


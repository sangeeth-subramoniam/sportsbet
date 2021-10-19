from django.shortcuts import render
from .models import sportinfo

# Create your views here.
def dashboardhome(request):
    return render(request, 'dashboard/dashboardhome.html')

def gameroom(request,pk):

    sport = sportinfo.objects.get(sport_name = pk)

    context = {
        'sport' : sport
    }
    return render(request, 'dashboard/gameroom.html' , context)
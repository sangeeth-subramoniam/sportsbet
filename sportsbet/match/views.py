from django.shortcuts import redirect, render
from structure.models import match

# Create your views here.
def matchhome(request,pk):

    matches = match.objects.all().filter(sport__sportname = 'Cricket')

    context = {
        'matches' : matches
    }

    return render(request, 'matches/match_list.html' , context)
from django.shortcuts import render,redirect
from structure.models import player,match
from django.db.models import Q
# Create your views here.
def cricket_team_create(request , pk):

    cur_match = match.objects.get(id = pk)

    ongoing_match = []
    ongoing_match.append(cur_match.id)
    
    print(cur_match)

    team1 = cur_match.team1
    team2 = cur_match.team2
    
    wkt = player.objects.all().filter(~Q(inmatch__in = ongoing_match) , position = 'WKT')
    all = player.objects.all().filter(~Q(inmatch__in = ongoing_match) , position = 'both')
    bat = player.objects.all().filter(~Q(inmatch__in = ongoing_match) , position = 'batsman')
    bow = player.objects.all().filter(~Q(inmatch__in = ongoing_match) , position = 'bowler')

    
    mysquad = player.objects.all().filter(inmatch__in = ongoing_match)
    print(mysquad)

    print(team2)
    context = {
        'cur_match' : cur_match,
        'wkt' : wkt,
        'all' : all,  
        'bat' : bat,  
        'bow' : bow,  
        'team1' : team1,  
        'team2' : team2,  
        'mysquad' : mysquad
    }
    
    return render(request,'teams/cricket/create_team.html' , context)



def cricket_add_to_squad(request,playerid,matchid ):
    player_to_add = player.objects.get( id = playerid )
    templist = []
    print('templist before append = ' , templist)
    for items in player_to_add.inmatch.all():
        templist.append(items)
    
    print('templist after append = ' , templist)
    mat = match.objects.get(id = matchid)
    if mat not in templist:
        player_to_add.inmatch.add(mat)
        player_to_add.save()
        print('added match ', matchid)
    else:
        player_to_add.inmatch.remove(mat)
        player_to_add.save()
        print('removed match ', matchid)

    print('player to add is ' , player_to_add.playername )
    return redirect('team:cricket_team_create' , matchid  )





def football_team_create(request):
    
    team1 = player.objects.all().filter(team__teamname = 'India')
    print(team1)
    context = {
        'team1' : team1 , 
    }
    
    return render(request,'teams/football/create_team.html' , context)
from django.shortcuts import render

# Create your views here.
def dashboardhome(request):
    return render(request, 'dashboard/dashboardhome.html')

def gameroom(request):
    return render(request, 'dashboard/gameroom.html')
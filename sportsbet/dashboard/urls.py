from django.urls import path,include
from . import views
 
app_name = 'dashboard'
urlpatterns = [
    path('', views.dashboardhome , name = "dashboardhome"),
    path('gameroom', views.gameroom , name = "gameroom"),
]

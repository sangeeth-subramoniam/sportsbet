from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'team'
urlpatterns = [
    path('cricket/<pk>', views.cricket_team_create , name = "cricket_team_create"),
    path('cric_add_to_squad/<int:playerid>/<int:matchid>', views.cricket_add_to_squad , name = "cricket_add_to_squad"),
    path('football/', views.football_team_create , name = "football_team_create"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

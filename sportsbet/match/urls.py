from django.urls import path,include
from . import views

app_name = 'match'
urlpatterns = [
    path('<pk>/', views.matchhome , name = "matchhome"),
]

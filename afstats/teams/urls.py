from django.urls import path
from . import views

urlpatterns = [
    path('team_add', views.team_add, name='team_add'),
    path('teams/', views.teams, name='teams'),
]

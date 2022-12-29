from django.urls import path
from . import views

urlpatterns = [
    path('team_add', views.team_add, name='team_add'),
]

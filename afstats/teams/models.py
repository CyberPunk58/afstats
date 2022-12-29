from django.db import models

class Team(models.Model):
    title = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    team_logo = models.ImageField (upload_to='teams/logo')
    color = models.CharField(max_length=30)
    reserve_color = models.CharField(max_length=30)
    url = models.URLField(blank=True)
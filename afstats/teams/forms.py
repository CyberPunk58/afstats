from .models import Team, Match
from django.forms import ModelForm, TextInput, ImageField

class TeamForm(ModelForm):
    class Meta:
        model = Team
        fields = ['title', 'city']


        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название команды'
            }),

            'city': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Город'
            }),

        }


class MatchTeam(ModelForm):
    class Meta:
        model = Match
        fields = ['team_1']


        widgets = {
            'team_1': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название командыassss'
            }),

        }
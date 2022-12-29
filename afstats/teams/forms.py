from .models import Team
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
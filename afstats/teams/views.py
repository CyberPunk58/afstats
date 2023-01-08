from django.shortcuts import render
from .models import Team
from .forms import TeamForm, MatchTeam

# Create your views here.

def teams(request):
    return render(request, 'teams/teams.html')

def team_add(request):
    error = ""
    if request.method == 'POST':
        form = TeamForm(request.POST)
        match_form = MatchTeam(request.POST)
        if form.is_valid():
            form.save()

        else:
            error = "Форма неверна"


    form = TeamForm()
    match_form = MatchTeam()

    data = {
        'form': form,
        'error': error,
        'match_form': match_form,
    }

    return render(request, 'teams/team_add.html', data)

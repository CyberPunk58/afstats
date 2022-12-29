from django.shortcuts import render
from .models import Team
from .forms import TeamForm

# Create your views here.

def teams(request):
    pass

def team_add(request):
    error = ""
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()

        else:
            error = "Форма неверна"


    form = TeamForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'teams/team_add.html', data)

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from gameplay.models import Game
from .forms import InvitationForm


@login_required
def home(request):
    my_games = Game.objects.games_for_user(request.user)
    active_games = my_games.active()
    drew_games = my_games.drew_games()

    return render(request, "player/home.html", {"ngames": Game.objects.count(),
                                                "games": active_games,
                                                "drew_games": drew_games})


@login_required
def new_invitation(request):

    if request.method == "POST":
        form = InvitationForm(data=request.POST)
        if form.is_valid():
            form.save()
            redirect("player_home")
    else:
        form = InvitationForm()

    return render(request, "player/new_invitation_form.html", {"form": form})

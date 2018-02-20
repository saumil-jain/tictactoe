from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

from gameplay.models import Game
from .forms import InvitationForm
from .models import Invitation


@login_required
def home(request):
    my_games = Game.objects.games_for_user(request.user)
    active_games = my_games.active()
    drew_games = my_games.drew_games()
    invitations = request.user.invitations_received.all()

    return render(request, "player/home.html", {"ngames": Game.objects.count(),
                                                "games": active_games,
                                                "drew_games": drew_games,
                                                "invitations": invitations})


@login_required
def new_invitation(request):
    if request.method == "POST":
        invitation = Invitation(from_user=request.user)
        form = InvitationForm(instance=invitation, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("player_home")
    else:
        form = InvitationForm()

    return render(request, "player/new_invitation_form.html", {"form": form})


@login_required
def accept_invitation(request, id):
    # retrieve the invitation object
    invitation = get_object_or_404(Invitation, pk=id)

    if request.user != invitation.to_user:
        raise PermissionDenied

    game = None

    if request.method == "POST":
        if "accept" in request.POST:
            game = Game.objects.create(
                first_player=invitation.to_user,
                second_player=invitation.from_user
            )

        # in any case, whether the invitation was accepted or
        # rejected, delete it
        invitation.delete()

        if game:
            # passing the object to redirect will call the
            # object's get_absolute_url method
            return redirect(game)
        else:
            # if invitation was declined, no game object was
            # created, hence redirect to player home
            return redirect("player_home")
    else:
        return render(request, "player/accept_invitation_form.html", {"invitation": invitation})

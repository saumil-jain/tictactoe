from django.db import models
from django.contrib.auth.models import User


class Game(models.Model):
    first_player = models.ForeignKey(User, on_delete=models.CASCADE, related_name="games_first_player")
    second_player = models.ForeignKey(User, on_delete=models.CASCADE, related_name="games_second_player")

    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(auto_now=True)


class Move(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    comment = models.CharField(max_length=300, blank=True)
    by_first_player = models.BooleanField()
    status = models.CharField(max_length=1, default='F')

    game = models.ForeignKey(Game, on_delete=models.CASCADE)

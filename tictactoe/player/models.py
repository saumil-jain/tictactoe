from django.db import models

from django.contrib.auth.models import User


class Invitation(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="invitations_sent")
    to_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="invitations_received",
        verbose_name="User to invite",
        help_text="Please select a user you want to play a game with."
    )
    message = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="Optional Message",
        help_text="Add an optional friendly invite message!"
    )
    timestamp = models.DateTimeField(auto_now_add=True)

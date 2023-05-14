from django.db import models
from django.contrib.auth.models import AbstractUser


class FriendRequest(AbstractUser):
    senders = models.ManyToManyField('users.User', related_name="submitted_requests")
    receivers = models.ManyToManyField('users.User', related_name="requests_received")
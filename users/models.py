from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email =  email = models.EmailField(max_length=128, unique=True, null=False)
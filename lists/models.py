from django.db import models

class List(models.Model):
    name = models.CharField(max_length=128)

    creator = models.ForeignKey("users.User", on_delete=models.PROTECT, related_name="my_lists")
    users = models.ManyToManyField("users.User", related_name="lists")
    watchs = models.ManyToManyField("seasons.Seadon", related_name="lists")
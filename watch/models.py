from django.db import models

class Watch(models.Model):
    name = models.CharField(max_length=128)
    link = models.URLField(null=True, blank=True)
    imagem = models.URLField(null=True, blank=True)
    is_movie = models.BooleanField(default=True)

from django.db import models

class watch(models.Model):
    name = models.CharField(max_length=128)
    link = models.URLField()
    imagem = models.URLField()

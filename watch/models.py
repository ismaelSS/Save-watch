from django.db import models

class Watch(models.Model):
    name = models.CharField(max_length=128)
    link = models.URLField(null=True, black=True)
    imagem = models.URLField(null=True, black=True)

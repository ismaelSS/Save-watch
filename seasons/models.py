from django.db import models

class Season(models.Model):
    name = models.CharField(max_length=60)
    image = models.URLField(null=True, black=True)
    link = models.URLField(null=True, black=True)
    is_dubbed = models.BooleanField(default=False)

    watch = models.ForeignKey(
        "watch.Watch",
        on_delete=models.CASCADE,
        related_name="seasons",
    )



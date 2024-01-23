from django.db import models

# Create your models here.
class Kategoria(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Obiekt(models.Model):
    title = models.CharField(max_length=255)
    opis = models.CharField(max_length=255)

    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)

    kategoria = models.ForeignKey(
        "Kategoria",
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    def __str__(self):
        return f'<div id="obiekty"><div class="title">{self.title}</div><div class="latitude">{self.latitude}</div><div class="longitude">{self.longitude}</div><div class="kategoria">{self.longitude}</div></div>'

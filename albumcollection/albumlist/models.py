from django.db import models

# Create your models here.

RECORD_TYPES = (
    (1, "LP"),
    (2, "CD"),
    (3, "tape"),
    (4, "file"),
)

LOCATIONS = (
    (1, "shelf"),
    (2, "harddrive"),
    (3, "bandcamp"),
)


class Artist (models.Model):
    name = models.CharField(max_length=160, unique=True)

    def __str__(self):
        return f'{self.name}'


class Album (models.Model):
    band = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title = models.CharField(max_length=160)
    release_year = models.IntegerField()
    songs = models.TextField()
    type = models.IntegerField(choices=RECORD_TYPES, name="type", default=1)
    location = models.IntegerField(choices=LOCATIONS, name="location", default=1)

    def __str__(self):
        return f'"{self.title}", ({self.get_location_display()})'









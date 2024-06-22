from django.db import models

# Create your models here.

from django.db import models

class Entity(models.Model):
    url = models.URLField()
    artist_name = models.CharField(max_length=255)
    program_name = models.CharField(max_length=255)
    artist_role = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    time = models.CharField(max_length=255)
    auditorium = models.CharField(max_length=255)

    def __str__(self):
        return self.artist_name
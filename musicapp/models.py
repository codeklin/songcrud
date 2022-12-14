from datetime import datetime, date
from email.policy import default
#from time import timezone
from django.db import models
#from django.utils import timezone
# Create your models here.


class Artiste(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=200)
    age = models.IntegerField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Song(models.Model):
    Artiste = models.ForeignKey(
        Artiste, on_delete=models.CASCADE, default='SOME STRING')
    title = models.CharField(max_length=100)
    date_released = models.DateField(
        auto_now_add=False, auto_now=False, blank=True)
    likes = models.CharField(max_length=100000000)
    artiste_id = models.IntegerField()

    def __str__(self):
        return self.title


class Lyric(models.Model):
    Artiste = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    content = models.TextField()
    song_id = models.IntegerField()

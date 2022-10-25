from django.db import models

# Create your models here.


class Artiste(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=200)
    age = models.IntegerField(max_length=100)


class Song(models.Models):
    title = models.CharField(max_length=100)
    date_released = models.DateField(max_length=100)
    likes = models.CharField(max_length=100)
    artiste_id = models.IntegerField(max_length=100)


class Lyric(models.Model):
    content = models.CharField(max_length=5000)
    song_id = models.IntegerField(max_length=100)

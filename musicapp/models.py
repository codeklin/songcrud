from django.db import models

# Create your models here.


class Artiste(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=200)
    age = models.IntegerField()


class Song(models.Model):
    title = models.CharField(max_length=100)
    date_released = models.DateField(max_length=100)
    likes = models.CharField(max_length=100)
    artiste_id = models.IntegerField()


class Lyric(models.Model):
    content = models.CharField(max_length=5000)
    song_id = models.IntegerField()

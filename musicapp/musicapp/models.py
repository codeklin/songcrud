from django.db import models


class Album(models.Model):
    artist = models.Charfield(max_lenght=200)
    album_title = models.Charfield(max_lenght=300)
    genre = models.Charfield(max_lenght=100)
    album_logo = models.Charfield(max_lenght=1000)


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models. CharField(max_length=250)

from django.db import models

# Create your models here.


class Artiste(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=200)
    age = models.IntegerField()

    def __str__(self):
        return self.first_name


class Song(models.Model):
    Artiste = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    date_released = models.DateField(max_length=100)
    likes = models.CharField(max_length=100000000)
    artiste_id = models.IntegerField()

    def __str__(self):
        return self.title


class Lyric(models.Model):
    content = models.CharField(max_length=5000)
    song_id = models.IntegerField()

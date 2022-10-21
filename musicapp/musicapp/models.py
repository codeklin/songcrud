from django.db import models

class Songs(models.Model):
    name = models.Charfield(max_lenght=100000)
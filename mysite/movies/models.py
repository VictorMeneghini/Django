from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=200)
    plot = models.TextField()
    poster = models.CharField(max_length=200)
    year = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    director = models.CharField(max_length=200)
    language = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.title}'

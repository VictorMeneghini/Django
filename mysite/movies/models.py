from django.contrib.auth.models import User
from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    post = models.CharField(max_length=200)
    year = models.IntegerField(default=0)
    genre = models.CharField(max_length=200)
    director = models.CharField(max_length=200)
    language = models.CharField(max_length=200)
    poster = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.title},{self.description}'


class UserMovies(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ManyToManyField(Movie)

    def __str__(self):
        return f'user_id: {self.user_id},movie_id: {self.movie_id}'


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='profile_image')

    def __str__(self):
        return f'user: {self.user},avatar: {self.avatar}'

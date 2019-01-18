from django.db import models
from django.contrib.auth.models import AbstractUser
from movies.models import Movie


class User(AbstractUser):
    avatar = models.ImageField(upload_to='profile_image', null=True)
    movies = models.ManyToManyField(Movie, null=True)

    def __str__(self):
        return f'user: {self.user},id {self.id}'

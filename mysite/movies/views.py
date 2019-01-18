from django.shortcuts import render, redirect
import requests
from .models import Movie


def index(request):
    if request.user.is_authenticated:
        return render(request, 'movies/index.html')
    else:
        return render(request, 'authentication/index.html')


def search_movie(request):
    search = request.POST.get('search')
    r = requests.get(
        'http://www.omdbapi.com/?t={movie}&apikey=b46e268f'
        .format(movie=search))
    if r.status_code == requests.codes.ok:
        r = r.json()
        movie_object = {
                'title': r.get('Title', 'No title'),
                'plot': r.get('Plot', 'No plot'),
                'poster': r.get('Poster', 'No poster'),
                'year': r.get('Year', 'No year'),
                'genre': r.get('Genre', 'No genre'),
                'director': r.get('Director', 'No director'),
                'language': r.get('Language', 'No Language')
            }
        Movie.objects.get_or_create(**movie_object)

    return render(request,
                  'movies/movie_description.html',
                  {
                      'movie': r,
                      'error': r
                  }
                  )


def add_favorite(request):
    print(request)
    return redirect('movies:index')
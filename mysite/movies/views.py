from django.shortcuts import render
import requests
from .models import UserProfile
from django.contrib.auth.models import User


def index(request):
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user_id = request.user.id)
        return render(request, 'movies/index.html', {'profile': profile})
    else:
        return render(request, 'authentication/index.html')


def search_movie(request):
    print(request.POST)
    search = request.POST.get('search')
    print(search)
    r = requests.get(
        'http://www.omdbapi.com/?t={movie}&apikey=b46e268f'.format(movie=search))
    if r.status_code == requests.codes.ok:
        print(r.json())
        print(r.headers['content-type'])

    return render(request,
                  'movies/movie_description.html',
                  {
                      'movie': r.json(),
                      'error': r.json()
                  }
                  )

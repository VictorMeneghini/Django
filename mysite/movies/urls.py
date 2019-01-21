from django.urls import path
from django.contrib.auth.decorators import login_required


from . import views

app_name = 'movies'
urlpatterns = [
    path('', login_required(views.index), name='index'),
    path('search_movie/', views.search_movie, name="search_movie"),
    path('<str:movie_title>/add_favorite/',
         views.add_favorite, name="add_favorite"),
    path('<str:movie_title>/remove_favorite/',
         views.remove_favorite, name="remove_favorite")
]

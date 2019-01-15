from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def index(request):
    if request.user.is_authenticated:
        return render(request, 'movies/index.html')
    else:
        return render(request, 'authentication/index.html')


def login_user(request):
    print(request.POST)
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    print(user)
    if user:
        login(request, user)
        return redirect('movies:index')
    else:
        return render(request, 'authentication/index.html')


def welcome(request):
    return render(request, 'authentication/welcome.html')


def signin_user(request):
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    user = User.objects.create_user(
        username,
        email,
        password
    )
    user.save()
    return redirect('movies:index')


def logout_user(request):
    logout(request)
    return render(request, 'authentication/index.html')

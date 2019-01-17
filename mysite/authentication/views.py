from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from movies.models import UserProfile
from django.http import HttpResponseRedirect

from .forms import AuthUser, SigninUser


def login_user(request):
    if request.user.is_authenticated:
        return redirect('movies:index')
    else: 
        if request.method == 'POST':
            form = AuthUser(request.POST)

            if form.is_valid():
                username = request.POST.get('username')
                password = request.POST.get('password')
                user = authenticate(request, username=username, password=password)
                if user:
                    login(request, user)
                    return redirect('movies:index')
                else:
                    return render(request, 'authentication/login_user.html', {'form': form, 'erro': "User Invalid"})  
        else:
            form = AuthUser()
            return render(request, 'authentication/login_user.html', {'form': form}) 


def signin_user(request):
    if request.user.is_authenticated:
        return redirect('movies:index')
    else:
        if request.method == 'POST':
            form = SigninUser(request.POST, request.FILES)

            if form.is_valid():
                username = request.POST.get('username')
                email = request.POST.get('email')
                password = request.POST.get('password')
                user = User.objects.create_user(
                    username,
                    email,
                    password
                )
                user.save()
                user_profile = UserProfile(user=user, avatar=request.FILES.get('file'))
                user_profile.save()
                return redirect('movies:index')
            else:
                print('invalid form')
                form = SigninUser()
                return render(request, 'authentication/signin_user.html', {'form': form})    
        else:
            form = SigninUser()
            return render(request, 'authentication/signin_user.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('authentication:login_user')

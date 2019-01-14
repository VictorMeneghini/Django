from django.urls import path

from . import views

app_name = 'authentication'
urlpatterns = [
    path('', views.index, name='index'),
    path('login_user/', views.login_user, name='login_user'),
    path('welcome/', views.welcome, name='welcome'),
    path('signin_user/', views.signin_user, name="signin_user"),
    path('logout_user/', views.logout_user, name="logout_user")
]

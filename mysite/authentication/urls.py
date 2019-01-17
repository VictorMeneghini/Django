from django.urls import path

from . import views

app_name = 'authentication'
urlpatterns = [
    path('', views.login_user, name='login_user'),
    path('signin_user/', views.signin_user, name="signin_user"),
    path('logout_user/', views.logout_user, name="logout_user"),
]
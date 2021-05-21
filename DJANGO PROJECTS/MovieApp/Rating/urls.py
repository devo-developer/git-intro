from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('movies/', views.movies, name='movies'),
    path('details/', views.details, name='details'),
    path('home/', views.home, name='home'),
]

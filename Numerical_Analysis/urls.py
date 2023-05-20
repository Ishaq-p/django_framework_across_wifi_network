from django.urls import path
from .views import *
from django.contrib import admin
from django.contrib import admin


urlpatterns = [
    path('', home1, name='home1'),
    path('bisection/', bisection, name='bisection'),
    path('horners/',   horners,   name='horners'),
    path('FPI/',       FPI,       name='FPI'),
    path('newtons/',   newtons,   name='newtons'),

    
]


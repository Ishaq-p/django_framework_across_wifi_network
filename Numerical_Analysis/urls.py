from django.urls import path
from .views import *
from django.contrib import admin
from django.contrib import admin


urlpatterns = [
    path('', home1, name='home1'),
    path('bisection/',    bisection,    name='bisection'),
    path('horners/',      horners,      name='horners'),
    path('FPI/',          FPI,          name='FPI'),
    path('newtons/',      newtons,      name='newtons'),
    path('secant/',       secant,       name='secant'),
    path('regula_falsi/', regula_falsi, name='regula_falsi'),
    path('falsi_fpi/', falsi_fpi, name='falsi_fpi'),


    
]


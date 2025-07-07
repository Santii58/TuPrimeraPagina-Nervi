from django.contrib import admin
from django.urls import path
from .views import inicio, cursos, alumnos, profesores

urlpatterns = [

    path('inicio/', inicio, name='inicio'),
    path('cursos/', cursos, name='cursos'),
    path('alumnos/', alumnos, name='alumnos'),
    path('profesores/', profesores, name='profesores'),
]
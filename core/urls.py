from django.contrib import admin
from django.urls import path
from .views import padre

urlpatterns = [
    path('', padre, name='inicio'),
    path('cursos/', padre, name='cursos'),
    path('alumnos/', padre, name='alumnos'),
    path('profesores/', padre, name='profesores'),
]
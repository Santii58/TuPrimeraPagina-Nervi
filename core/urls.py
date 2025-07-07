from django.contrib import admin
from django.urls import path
from .views import inicio, cursos, alumnos, profesores, agregar_curso, agregar_alumno, agregar_profesor

urlpatterns = [

    path('inicio/', inicio, name='inicio'),
    path('cursos/', cursos, name='cursos'),
    path('alumnos/', alumnos, name='alumnos'),
    path('profesores/', profesores, name='profesores'),
    path('agregar_curso/', agregar_curso, name='agregar_curso'),
    path('agregar_alumno/', agregar_alumno, name='agregar_alumno'),
    path('agregar_profesor/', agregar_profesor, name='agregar_profesor'),
]
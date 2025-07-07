from django.shortcuts import render
from django.http import HttpResponse
from .models import Cursos, Alumnos, Profesores

# Create your views here.

def inicio(request):
    return render(request, 'core/inicio.html')

def cursos(request):
    cursos = Cursos.objects.all()
    return render(request, 'core/cursos.html', {'cursos': cursos})

def alumnos(request):
    alumnos = Alumnos.objects.all()
    return render(request, 'core/alumnos.html', {'alumnos': alumnos})

def profesores(request):
    profesores = Profesores.objects.all()
    return render(request, 'core/profesores.html', {'profesores': profesores})



from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def padre(request):
    return render(request, 'core/padre.html')

def cursos(request):
    return render(request, 'core/cursos.html')

def alumnos(request):
    return render(request, 'core/alumnos.html')

def docentes(request):
    return render(request, 'core/docentes.html')

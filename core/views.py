from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def padre(request):
    return render(request, 'core/padre.html')

def alumnos(request):
    return HttpResponse("core/alumnos.html")

def profesores(request):
    return HttpResponse("core/profesores.html")

def cursos(request):
    return HttpResponse("core/cursos.html")
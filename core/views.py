from django.shortcuts import render, redirect
from .models import Cursos, Alumnos, Profesores
from .forms import CursosForm, AlumnosForm, ProfesoresForm

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

def agregar_curso(request):
    if request.method == 'POST':
        form = CursosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cursos')
    else:
        form = CursosForm()
    return render(request, 'core/formulario/agregar_curso.html', {'form': form})

def agregar_alumno(request):
    if request.method == 'POST':
        form = AlumnosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alumnos')
    else:
        form = AlumnosForm()
    return render(request, 'core/formulario/agregar_alumno.html', {'form': form})

def agregar_profesor(request):
    if request.method == 'POST':
        form = ProfesoresForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profesores')
    else:
        form = ProfesoresForm()
    return render(request, 'core/formulario/agregar_profesor.html', {'form': form})
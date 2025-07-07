from django import forms

class CursosForm(forms.Form):
    nombre = forms.CharField(max_length=100, label='Nombre del Curso')
    descripcion = forms.CharField(widget=forms.Textarea, label='Descripción')
    fecha_inicio = forms.DateTimeField(label='Fecha de Inicio')
    fecha_fin = forms.DateTimeField(label='Fecha de Fin')

class AlumnosForm(forms.Form):
    nombre = forms.CharField(max_length=100, label='Nombre del Alumno')
    apellido = forms.CharField(max_length=100, label='Apellido del Alumno')
    email = forms.EmailField(label='Email del Alumno')
    fecha_nacimiento = forms.DateField(label='Fecha de Nacimiento')

class ProfesorsForm(forms.Form):
    nombre = forms.CharField(max_length=100, label='Nombre del Profesor')
    apellido = forms.CharField(max_length=100, label='Apellido del Profesor')
    email = forms.EmailField(label='Email del Profesor')
    especialidad = forms.CharField(max_length=100, label='Especialidad del Profesor')

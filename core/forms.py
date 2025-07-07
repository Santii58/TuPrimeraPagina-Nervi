from django import forms
from .models import Cursos, Alumnos, Profesores

class CursosForm(forms.ModelForm):
    class Meta:
        model = Cursos
        fields = ['nombre', 'descripcion', 'fecha_inicio', 'fecha_fin']  # Incluye los campos de fecha

class AlumnosForm(forms.ModelForm):
    class Meta:
        model = Alumnos
        fields = ['nombre', 'apellido', 'email', 'fecha_nacimiento']

class ProfesoresForm(forms.ModelForm):
    class Meta:
        model = Profesores
        fields = ['nombre', 'apellido', 'email', 'especialidad']
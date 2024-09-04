from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Profesor, Curso, Estudiante
from django.contrib.auth.mixins import LoginRequiredMixin




# VISTAS BASADAS EN CLASES - Profesores
class ProfesoresListView(LoginRequiredMixin,ListView):
    model = Profesor
    context_object_name = "profesores"
    template_name = "proyectofinal/Vistas_Clases/profesor_list.html"

    
class ProfesoresDetailView(LoginRequiredMixin,DetailView):
    model = Profesor
    template_name = "leerProfesores.html"    


class ProfesoresCreateView(LoginRequiredMixin,CreateView):
    
    model = Profesor
    template_name = "proyectofinal/Vistas_Clases/agregarProfesores.html"
    success_url = reverse_lazy('List')
    fields = ['nombre', 'apellido', 'email', 'profesion']
    

class ProfesoresUpdateView(LoginRequiredMixin,UpdateView):
    model = Profesor
    success_url = reverse_lazy("List")
    template_name = "proyectofinal/Vistas_Clases/profesor_update.html"
    fields = ["nombre", "apellido", "email", "profesion"]    


class ProfesoresDeleteView(LoginRequiredMixin,DeleteView):
    model = Profesor
    context_object_name = "profesores"
    template_name = "proyectofinal/Vistas_Clases/profesor_confirm_delete.html"
    success_url = reverse_lazy('List')
    



# VISTAS BASADAS EN CLASES - Cursos
class CursoListView(LoginRequiredMixin,ListView):
    model = Curso
    context_object_name = "cursos"
    template_name = "proyectofinal/Vistas_Clases/curso_list.html"

    
class CursoDetailView(LoginRequiredMixin,DetailView):
    model = Curso
    template_name = "leerProfesores.html"    


class CursoCreateView(LoginRequiredMixin,CreateView):
    
    model = Curso
    template_name = "proyectofinal/Vistas_Clases/agregar_cursos.html"
    success_url = reverse_lazy('CursoList')
    fields = ['nombre', 'camada']

    
    

class CursoUpdateView(LoginRequiredMixin,UpdateView):
    model = Curso
    success_url = reverse_lazy("CursoList")
    template_name = "proyectofinal/Vistas_Clases/curso_update.html"
    fields = ['nombre', 'camada'] 


class CursoDeleteView(LoginRequiredMixin,DeleteView):
    model = Curso
    context_object_name = "cursos"
    template_name = "proyectofinal/Vistas_Clases/curso_confirm_delete.html"
    success_url = reverse_lazy('CursoList')
    


# VISTAS BASADAS EN CLASES - Estudiantes
class EstudianteListView(LoginRequiredMixin,ListView):
    model = Estudiante
    context_object_name = "estudiantes"
    template_name = "proyectofinal/Vistas_Clases/estudiantes_list.html"

    
class EstudianteDetailView(LoginRequiredMixin,DetailView):
    model = Estudiante
    template_name = "leerProfesores.html"    


class EstudianteCreateView(LoginRequiredMixin,CreateView):
    
    model = Estudiante
    template_name = "proyectofinal/Vistas_Clases/agregar_estudiantes.html"
    success_url = reverse_lazy('EstudianteList')
    fields = ["nombre", "apellido", "email"]
    

class EstudianteUpdateView(LoginRequiredMixin,UpdateView):
    model = Estudiante
    success_url = reverse_lazy("EstudianteList")
    template_name = "proyectofinal/Vistas_Clases/estudiantes_update.html"
    fields = ["nombre", "apellido", "email"] 


class EstudianteDeleteView(LoginRequiredMixin,DeleteView):
    model = Estudiante
    context_object_name = "estudiantes"
    template_name = "proyectofinal/Vistas_Clases/estudiantes_confirm_delete.html"
    success_url = reverse_lazy('EstudianteList')
    


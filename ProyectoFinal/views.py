from django.shortcuts import render
from django.http import HttpResponse
from ProyectoFinal.models import Curso
from django.contrib.auth.decorators import login_required


def inicio(request):
    return render(request,'proyectofinal/index.html')


@login_required
def cursos(request):
 return render(request, 'proyectofinal/cursos.html')


@login_required
def profesores(request):
 return render(request,'proyectofinal/profesores.html')


@login_required
def estudiantes(request):
 return render(request, 'proyectofinal/estudiantes.html')




@login_required
def busqueda(request):
 return render(request, 'proyectofinal/busqueda.html')

    

@login_required
def buscar(request): 
     if request.GET["camada"]:
          camada = request.GET['camada']
          cursos = Curso.objects.filter(camada__icontains=camada)
          return render(request,"proyectofinal/resultadoBusqueda.html", {"cursos":cursos, "camada":camada})
     
     else:
          respuesta = "No enviaste datos"


          return HttpResponse(respuesta)
     


@login_required
def resultadoBusqueda(request):
 return render(request, 'proyectofinal/resultadoBusqueda.html')




from django.http import HttpResponse
from django.template import Template, Context, loader
from datetime import datetime
from ProyectoFinal.models import Curso

def saludo(request):
    return HttpResponse("Hola Django - Coder ")

def probando_template(request):

    nom = "Javier"
    ape = "Torres"
    lista_notas = [1,2,3,4,5,6,7,8,9,10,11,11,11]

    diccionario = { "nombre":nom, "apellido": ape, "hoy":datetime.now(), "notas":lista_notas}


    # mi_html = open('./Proyecto1/plantillas/template1.html')

    # plantilla = Template(mi_html.read())
    # mi_html.close()

    # mi_contexto = Context(diccionario)

    plantilla = loader.get_template('template1.html')

    documento = plantilla.render(diccionario)

    return HttpResponse(documento)


def agregar_curso(request, nom, cam):
    curso = Curso(nombre= nom, camada=cam)
    curso.save()

    return HttpResponse("Curso Agregado")


    

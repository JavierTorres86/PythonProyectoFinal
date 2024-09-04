from django import forms

class Curso(forms.Form):
    nombre = forms.CharField(max_length=40)
    camada = forms.IntegerField()



class agregarProfesores(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    email = forms.EmailField()
    profesion = forms.CharField(max_length=100)

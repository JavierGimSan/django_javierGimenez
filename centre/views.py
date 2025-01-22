from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    professor = {"name":"Roger", "surname":"Sobrino", "age":"17"}
    template = loader.get_template('index_centre.html')
    dades = template.render({'nombre':professor["name"], 'surname':professor["surname"], 'age':professor["age"]})
    return HttpResponse(dades)


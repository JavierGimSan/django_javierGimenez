from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


#Funció de prova
def index(request):
    template = loader.get_template('index_centre.html')
    return HttpResponse(template.render())

#Funció per a l'exercici 1, endpoint "/teachers"
def teachers(request):
    professors = [{"name":"Roger", "surname1":"Sobrino", "surname2":"Sobrino", "email":"roger.sobrino@iticbcn.cat", "curs": "2", "tutor": "si", "modules": "M07"},
                 {"name":"Oriol", "surname1":"Roca", "surname2":"Fabra", "email":"oriol.roca@iticbcn.cat", "curs": "2", "tutor": "no", "modules": "M06"},
                 {"name":"Juan Manuel", "surname1":"Sánchez", "surname2":"Bel", "email":"juan.sanchez@iticbcn.cat", "curs": "2", "tutor": "no", "modules": "M08"}
                 ]
    context = {'professors': professors}
    return render(request, 'teachers.html', context)

def students(request):
    alumnes = [{"name":"Victor Andrés", "surname1":"Fernández", "surname2":"Álvarez", "email":"2023_victor.fernandez@iticbcn.cat", "curs": "2", "modules": "M06, M07, M08, IA"},
               {"name":"Xavier", "surname1":"Porras", "surname2":"del Pino", "email":"2023_xavier.porras@iticbcn.cat", "curs": "2", "modules": "M06, M07, M08"},
               {"name":"Hugo", "surname1":"Sansegundo", "surname2":"Costantini", "email":"2023_hugo.sansegundo@iticbcn.cat", "curs": "2", "modules": "M06, M07, M08, Big Data"},
               {"name":" ", "surname1":" ", "surname2":" ", "email":" ", "curs": "2", "modules": " "}

               ]
    context = {'alumnes': alumnes}
    return render(request, 'students.html', context)
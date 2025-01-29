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
    professors = [
                 {"name":"Roger", "surname1":"Sobrino", "surname2":"Sobrino", "email":"roger.sobrino@iticbcn.cat", "curs": "2", "tutor": "si", "modules": "M07"},
                 {"name":"Oriol", "surname1":"Roca", "surname2":"Fabra", "email":"oriol.roca@iticbcn.cat", "curs": "2", "tutor": "no", "modules": "M06"},
                 {"name":"Juan Manuel", "surname1":"Sánchez", "surname2":"Bel", "email":"juan.sanchez@iticbcn.cat", "curs": "2", "tutor": "no", "modules": "M08"}
                 ]
    context = {'professors': professors}
    return render(request, 'teachers.html', context)

def students(request):
    alumnes = [
               {"name":"Victor Andrés", "surname1":"Fernández", "surname2":"Álvarez", "email":"2023_victor.fernandez@iticbcn.cat", "curs": "2", "modules": "M06, M07, M08, IA"},
               {"name":"Xavier", "surname1":"Porras", "surname2":"del Pino", "email":"2023_xavier.porras@iticbcn.cat", "curs": "2", "modules": "M06, M07, M08"},
               {"name":"Hugo", "surname1":"Sansegundo", "surname2":"Costantini", "email":"2023_hugo.sansegundo@iticbcn.cat", "curs": "2", "modules": "M06, M07, M08, Big Data"},
               {"name":"Adrián", "surname1":"Navarro", "surname2":"Pérez", "email":"2023_adrian.navarro@iticbcn.cat", "curs": "2", "modules": "M06, M07, M08"},
               {"name":"Javier", "surname1":"Giménez", "surname2":"Sánchez", "email":"2023_javier.gimenez@iticbcn.cat", "curs": "2", "modules": "M06, M07, M08"},
               {"name":"Daniel", "surname1":"Vallespin", "surname2":"Mellado", "email":"2023_daniel.vallespin@iticbcn.cat", "curs": "2", "modules": "M06, M07, M08"},
               {"name":"Milena", "surname1":"Vardumyan", "surname2":"Aleksanyan", "email":"2023_milena.vardumyan@iticbcn.cat", "curs": "2", "modules": "M06, M07, M08"},
               {"name":"Félix Bequet", "surname1":"Balbin", "surname2":"Silva", "email":"2023_felix.balbin@iticbcn.cat", "curs": "2", "modules": "M06, M07, M08"},
               {"name":"Albert", "surname1":"Penadés", "surname2":"Casajús", "email":"2023_albert.penades@iticbcn.cat", "curs": "2", "modules": "M06, M07, M08"},
               {"name":"Natalia", "surname1":"Casanellas", "surname2":"Blanquer", "email":"2023_natalia.casanellas@iticbcn.cat", "curs": "2", "modules": "M06, M07, M08"},   
               ]
    context = {'alumnes': alumnes}
    return render(request, 'students.html', context)

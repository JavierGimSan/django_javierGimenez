from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Student, Teacher

from .forms import StudentForm, TeacherForm




#Funció de prova
def index(request):
    template = loader.get_template('index_centre.html')
    return HttpResponse(template.render())


#Diccionaris d'alumnes i professors:

#----------PROFESSORS---------#
professors = [
             {"id":"1", "name":"Roger", "surname1":"Sobrino", "surname2":"Sobrino", "email":"roger.sobrino@iticbcn.cat", "curs": "2", "tutor": "si", "modules": "M07"},
             {"id":"2", "name":"Oriol", "surname1":"Roca", "surname2":"Fabra", "email":"oriol.roca@iticbcn.cat", "curs": "2", "tutor": "no", "modules": "M06"},
             {"id":"3", "name":"Juan Manuel", "surname1":"Sánchez", "surname2":"Bel", "email":"juan.sanchez@iticbcn.cat", "curs": "2", "tutor": "no", "modules": "M08"}
             ]

#------------ALUMNES----------#
alumnes = [
           {"id":"1","name":"Victor Andrés", "surname1":"Fernández", "surname2":"Álvarez", "email":"2023_victor.fernandez@iticbcn.cat", "curs": "2", "modules": "M06, M07, M08, IA"},
           {"id":"2","name":"Xavier", "surname1":"Porras", "surname2":"del Pino", "email":"2023_xavier.porras@iticbcn.cat", "curs": "2", "modules": "M06, M07, M08"},
           {"id":"3","name":"Hugo", "surname1":"Sansegundo", "surname2":"Costantini", "email":"2023_hugo.sansegundo@iticbcn.cat", "curs": "2", "modules": "M06, M07, M08, Big Data"},
           {"id":"4","name":"Adrián", "surname1":"Navarro", "surname2":"Pérez", "email":"2023_adrian.navarro@iticbcn.cat", "curs": "2", "modules": "M06, M07, M08"},
           {"id":"5","name":"Javier", "surname1":"Giménez", "surname2":"Sánchez", "email":"2023_javier.gimenez@iticbcn.cat", "curs": "2", "modules": "M06, M07, M08"},
           {"id":"6","name":"Daniel", "surname1":"Vallespin", "surname2":"Mellado", "email":"2023_daniel.vallespin@iticbcn.cat", "curs": "2", "modules": "M06, M07, M08"},
           {"id":"7","name":"Milena", "surname1":"Vardumyan", "surname2":"Aleksanyan", "email":"2023_milena.vardumyan@iticbcn.cat", "curs": "2", "modules": "M06, M07, M08"},
           {"id":"8","name":"Félix Bequet", "surname1":"Balbin", "surname2":"Silva", "email":"2023_felix.balbin@iticbcn.cat", "curs": "2", "modules": "M06, M07, M08"},
           {"id":"9","name":"Albert", "surname1":"Penadés", "surname2":"Casajús", "email":"2023_albert.penades@iticbcn.cat", "curs": "2", "modules": "M06, M07, M08"},
           {"id":"10","name":"Natalia", "surname1":"Casanellas", "surname2":"Blanquer", "email":"2023_natalia.casanellas@iticbcn.cat", "curs": "2", "modules": "M06, M07, M08"},   
           ]

#Funció per a l'exercici 1, endpoint "/teachers"
def teachers(request):
    context = {'professors': professors}
    return render(request, 'teachers.html', context)

#Funció per a l'exercici 1, endpoint "/alumnes"
def students(request):    
    context = {'alumnes': alumnes}
    return render(request, 'students.html', context)

#Funció per a l'exercici 2, endpoint "/teachers/{id}"
def teacher(request, pk):
    teacher_Obj = None
    for i in professors:
        if i['id'] == pk:
            teacher_Obj = i
    return render(request, 'teacher.html', {'teacher': teacher_Obj})

#Funció per a l'exercici 2, endpoint "/students/{id}"
def student(request, pk):
    student_Obj = None
    for i in alumnes:
        if i['id'] == pk:
            student_Obj = i
    return render(request, 'student.html', {'student': student_Obj})

#Funcions per a l'exercici 3

# def students(request, pk):
#     students = Student.objects.get(id=pk)
#     context = {'students': students}
#     return render(request, 'students.html', context)

# def teachers(request, pk):
#     teachers = Teacher.objects.get(id=pk)
#     context = {'teachers': teachers}
#     return render(request, 'teachers.html', context)


def student_form(request):
    form = StudentForm()
    context = {'form':form}
    return render(request, 'formStudent.html', context)

def teacher_form(request):
    form = TeacherForm()
    context = {'form':form}
    return render(request, 'formTeacher.html', context)
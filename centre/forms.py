from django.forms import ModelForm
from .models import Student, Teacher

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'surname1', 'surname2', 'email', 'curs', 'modules']
        # fields = '__all__'


class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = ['name', 'surname1', 'surname2', 'email', 'curs', 'tutor', 'modules']
        # fields = '__all__'
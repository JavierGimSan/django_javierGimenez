from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('teachers', views.teachers, name='teachers'),
    path('students', views.students, name='students'),
    path('teachers/<str:pk>/', views.teacher, name='teacher'),
    path('students/<str:pk>/', views.student, name='student'),
    path('student-form', views.student_form, name='student-form'),
    path('teacher-form', views.teacher_form, name='teacher-form')
]
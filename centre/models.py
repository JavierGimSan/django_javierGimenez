from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    surname1 = models.CharField(max_length=100)
    surname2 = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    curs = models.CharField(max_length=100)
    modules = models.CharField(max_length=100)

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    surname1 = models.CharField(max_length=100)
    surname2 = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    curs = models.CharField(max_length=100)
    tutor = models.BooleanField(default=False)
    modules = models.CharField(max_length=100)

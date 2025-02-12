from django.db import models

# Crear el model necessari per al bon funcionament de l’aplicació.
# 4 camps:
# id (primary key i autogenerat).
# 1 camp ha de ser unique
# 3 camps amb max_length.

class User(models.Model):
    name = models.CharField(max_length=100, unique=True)
    surname1 = models.CharField(max_length=100)
    age = models.CharField(max_length=3)
    email = models.CharField(max_length=100)

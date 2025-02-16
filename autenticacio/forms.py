from django.forms import ModelForm
from .models import User

#Camps que sortirán al formulari

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']
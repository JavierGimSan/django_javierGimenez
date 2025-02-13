from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm

def index(request):
    template = loader.get_template('paginaInici.html')
    return HttpResponse(template.render())

def login(request):
    form = UserForm()
    context = {'form':form}
    return render(request, 'login.html', context)


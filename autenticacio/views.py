from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    template = loader.get_template('paginaInici.html')
    return HttpResponse(template.render())

def login(request):
    context = {'form':form}
    return render(request, 'login.html', context)


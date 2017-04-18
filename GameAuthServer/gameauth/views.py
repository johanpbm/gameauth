#from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hola, esta es la aplicaci&oacute;n de Game Authoring")
# Create your views here.

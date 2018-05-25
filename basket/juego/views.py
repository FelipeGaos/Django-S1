from django.shortcuts import render
from django.http import HttpResponse
from juego.models import jugador

# Create your views here.
def index(request):
	return render(request,"views/index.html")


def list_jugadores(request):
	jugadores = jugador.objects.all()
	lista_jugadores = {'jugadores':jugadores }
	return render(request,"views/list_jugadores.html",lista_jugadores)
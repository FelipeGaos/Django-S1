from django.contrib import admin

# Register your models here.

from .models import jugador,equipo,entrenador

admin.site.register(jugador)
admin.site.register(equipo)
admin.site.register(entrenador)
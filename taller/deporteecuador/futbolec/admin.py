from django.contrib import admin

# Importar las clases del modelo
from futbolec.models import Equipo_Futbol, Jugador, Campeonato, Campeonato_Equipos

# Se crea una clase que hereda
admin.site.register(Equipo_Futbol)


class JugadorAdmin(admin.ModelAdmin):
    # listado de atributos que se mostrará
    # por cada registro
    # se deja de usar la representación (str) 
    # de la clase 
    list_display = ('nombre', 'posicion', 'numero_camisa', 'sueldo', 'equipo')
    search_fields = ('nombre', 'equipo__nombre')

admin.site.register(Jugador, JugadorAdmin)

admin.site.register(Campeonato)

class Campeonato_Equiposdmin(admin.ModelAdmin):
    # listado de atributos que se mostrará
    # por cada registro
    # se deja de usar la representación (str) 
    # de la clase 
    list_display = ('anio', 'equipo', 'campeonato')
    search_fields = ('equipo__nombre', 'campeonato__nombre')

admin.site.register(Campeonato_Equipos, Campeonato_Equiposdmin)


from django.db import models

# Create your models here.

class Equipo_Futbol(models.Model):

    nombre = models.CharField("Nombre de Equipo", max_length=30)
    siglas = models.CharField(max_length=30)
    userTwitter = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return "%s - %s - %s" % (self.nombre, 
                self.siglas,
                self.userTwitter)


class Jugador(models.Model):
    """
    """
    opciones_posicionCamp= (
        ('1', 'Arquero'),
        ('2', 'Centro'),
        ('3', 'Delantero'),
        ('4', 'Defensa'),
        )

    nombre = models.CharField("Nombre de Jugador", max_length=30)
    posicion = models.CharField(max_length=30, \
            choices=opciones_posicionCamp) 
    numero_camisa = models.IntegerField("Numero Camiseta")
    sueldo = models.IntegerField("sueldo")
    equipo = models.ForeignKey(Equipo_Futbol, related_name='losjugadores', 
            on_delete=models.CASCADE)

    def __str__(self):
        return "%s - Posicion: %s - Numero Jersey: %d - Sueldo: %d - Equipo(%s)" % (self.nombre, 
        		self.posicion, 
        		self.numero_camisa, 
        		self.sueldo, 
        		self.equipo)


class Campeonato(models.Model):

    nombre= models.CharField("Nombre de Campeonato", max_length=30)
    nombre_auspiciante = models.CharField(max_length=30)


    def __str__(self):
        return "%s - %s" % (self.nombre, 
                self.nombre_auspiciante)

class Campeonato_Equipos(models.Model):

    anio = models.IntegerField("año")
    equipo = models.ForeignKey(Equipo_Futbol, related_name='loscampeonatos', 
            on_delete=models.CASCADE)
    campeonato = models.ForeignKey(Campeonato, related_name='campeonatos', 
            on_delete=models.CASCADE)


    def __str__(self):
        return "Año: %s - Equipo(%s) - Campeonato(%s)" % (self.anio, 
                self.equipo, self.campeonato)
from django.db import models

# Create your models here.
class Book(models.Model):
	class Sexo(models.IntegerChoices):
		Masculino = 1
		Femenino = 2
	class Pais(models.IntegerChoices):
		Colombia = 1
		Venezuela = 2
		Argentina = 3
		Phile = 4
		peru = 5
		Mexico = 6
		Brazil = 7
	class Acompanantes(models.IntegerChoices):
		Solo = 1
		Familia = 2
		Amigos = 3
		Compañeros = 4
		Otro = 5
	class Motivos(models.IntegerChoices):
		Visita_familiares = 1
		Vacaciones = 2
		Compras = 3
		Turismo_cultural = 4
		Asistencia_eventos_artisticos = 5
		Estudio_formacion = 6
		Salud_belleza = 7
		Religioso = 8
		Congresos_seminarios = 9
		Trabajo_remunerado = 10
		Trabajo_negocios_no_remunerado = 11
		Eventos_artisticos_deportivos = 12
		Transito = 13
		Otro = 14

	class Organizacion(models.IntegerChoices):
		Paquete_colombia = 1
		Paquete_pais_visita = 2
		Paquete_no_agencia_viaje = 3
		Cuenta_propia = 4
		Otro = 5

	class Servicios(models.IntegerChoices):
		Alojamiento = 1
		Transporte_internacional = 2
		Alimentos_bebidas = 3
		Culturales_entretenimiento = 4
		Deportivos_recreacionales = 5
		Tours_destino = 6
		Transporte_aereo_en_destino = 7
		Otro_transporte = 8
		Otro = 9

	pais = models.PositiveSmallIntegerField(choices=Pais.choices,null=True,blank=True)
	nacionalidad = models.CharField(max_length=100,null=True,blank=True)
	sexo = models.PositiveSmallIntegerField(choices=Sexo.choices,null=True,blank=True)
	edad = models.PositiveSmallIntegerField(null=True,blank=True)
	acompanantes = models.PositiveSmallIntegerField(choices=Acompanantes.choices,null=True,blank=True)
	numacompanantes = models.PositiveSmallIntegerField(null=True,blank=True)
	motivos = models.PositiveSmallIntegerField(choices=Motivos.choices,null=True,blank=True)
	organizacion = models.PositiveSmallIntegerField(choices=Organizacion.choices,null=True,blank=True)
	servicios = models.PositiveSmallIntegerField(choices=Servicios.choices,null=True,blank=True)

	def __str__(self):
		return self.pais

	def delete(self,*args,**kwargs):
		super().delete(*args,**kwargs)


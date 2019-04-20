# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from clientes_ms.models import Clientes
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime
import pytz

# Create your models here.

class Servicos(models.Model):
	"""docstring for Clientes"""
	class Meta:
		verbose_name_plural = "serviços"
	
	descricao = models.CharField(max_length=200)
	validade = models.IntegerField(default=30)
	entradas =  models.IntegerField(default=10)
	premio = models.TextField()

	def __str__(self):
		return self.descricao

class Registros(models.Model):
	"""docstring for Registros"""
	class Meta:
		verbose_name_plural = "registros"
	
	data = models.DateTimeField(default=timezone.now)
	servico = models.ForeignKey(Servicos, on_delete=models.CASCADE)
	cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
	status = models.BooleanField(default=True)

	def __str__(self):
		return self.data.strftime('%m/%d/%Y')

class Premios(models.Model):
	"""docstring for Premios"""
	class Meta:
		verbose_name_plural = "premios"
	
	data = models.DateTimeField(default=timezone.now)
	servico = models.ForeignKey(Servicos, on_delete=models.CASCADE)
	cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
	baixado = models.BooleanField(default=False)

	def __str__(self):
		return self.data.strftime('%m/%d/%Y')


@receiver(post_save, sender=Registros)
def ensure_profile_exists(sender, instance, **kwargs):
    cliente = instance.cliente
    validar_registros(cliente.cpf);

def validar_registros(cpf):
	print(cpf)
	registros = Registros.objects.filter(cliente__cpf = cpf)
	print(len(registros))
	contador = 0
	validos = []
	for aux in registros:
		dias = datetime.datetime.now(pytz.utc) - aux.data
		servico = aux.servico
		data_invalida = dias.days > servico.validade
		if (data_invalida):
			aux.status = False
			aux.save()
		elif((not data_invalida) and (not aux.status)):
			contador+=1
			validos.append(aux)
			if (contador>=servico.entradas):
				for aux in validos:
					aux.status = False
					aux.save()
				print("premio gerado")	# TO DO: Adicionar aqui a lógica de criação de novo registro
				premio = Premios()
				premio.baixado = False
				premio.cliente = aux.cliente
				premio.data = timezone.now()
				premio.servico = aux.servico
				premio.save()
				break    
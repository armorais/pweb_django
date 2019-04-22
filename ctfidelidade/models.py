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

	@property
	def valido(self):
		return ((datetime.datetime.now(pytz.utc) - self.data).days <= self.servico.validade)

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

	@property
	def valido(self):
		return ((datetime.datetime.now(pytz.utc) - self.data).days <= self.servico.validade)

	def __str__(self):
		return self.data.strftime('%m/%d/%Y')
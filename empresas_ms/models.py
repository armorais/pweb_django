from django.db import models
from ctfidelidade.models import Servicos

class Empresas(models.Model):

	"""docstring for Empresas"""
	class Meta:
		verbose_name_plural = "empresas"
	
	cnpj = models.CharField(max_length=15, )
	nome = models.CharField(max_length=200)
	servicos = models.ManyToManyField(Servicos)
	
	def __str__(self):
		return self.nome
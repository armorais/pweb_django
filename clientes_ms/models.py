from django.db import models

class Clientes(models.Model):
	"""docstring for Clientes"""
	class Meta:
		verbose_name_plural = "clientes"
	
	cpf = models.CharField(max_length=15, )
	nome = models.CharField(max_length=200)
	cep = models.CharField(max_length=15 )

	def __str__(self):
		return self.nome
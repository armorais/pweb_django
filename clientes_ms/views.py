from __future__ import unicode_literals
from clientes_ms.models import Clientes
from clientes_ms.serializers import ClientesSerializer
from rest_framework.views import  APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
import pycep_correios
from pycep_correios.excecoes import ExcecaoPyCEPCorreios

#
#	Clientes
#

class ClientesList(APIView):
	def get(self, request, format=None):
		clientes = Clientes.objects.all()
		serializer = ClientesSerializer(clientes, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = ClientesSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClientesDetail(APIView):

	def get_object(self, cpf):
		try:
			return Clientes.objects.get(cpf=cpf)
		except Clientes.DoesNotExist:
			raise Http404


	def get(self, request, cpf, format=None):
		cliente = self.get_object(cpf)
		serializer = ClientesSerializer(cliente)
		response = serializer.data
		response = Endereco.pegar_endereco(serializer.data['cep'], response)
		return Response(response, status=status.HTTP_201_CREATED)


class Endereco(object):
    @staticmethod
    def pegar_endereco(cep, response):
    	try:
    		endereco = pycep_correios.consultar_cep(cep)
    		response.update({"endereço":endereco['end']})
    		response.update({"bairro":endereco['bairro']})
    		response.update({"cidade":endereco['cidade']})
    		response.update({"estado":endereco['uf']})
    	except ExcecaoPyCEPCorreios as exc:
    		response.update({"endereço":"cep inválido"})
    	return response
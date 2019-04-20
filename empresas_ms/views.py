from __future__ import unicode_literals
from django.shortcuts import render
from empresas_ms.models import Empresas
from empresas_ms.serializers import EmpresasSerializer
from rest_framework.views import  APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

#
#	Empresas
#

class EmpresasList(APIView):
	def get(self, request, format=None):
		empresas = Empresas.objects.all()
		serializer = EmpresasSerializer(empresas, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = EmpresasSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmpresasDetail(APIView):

	def get_object(self, cnpj):
		try:
			return Empresas.objects.get(cnpj=cnpj)
		except Empresas.DoesNotExist:
			raise Http404


	def get(self, request, cnpj, format=None):
		empresa = self.get_object(cnpj)
		serializer = EmpresasSerializer(empresa)
		return Response(serializer.data, status=status.HTTP_201_CREATED)
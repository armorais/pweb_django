from __future__ import unicode_literals
from ctfidelidade.models import *
from ctfidelidade.serializers import *
from rest_framework.views import  APIView
from rest_framework.response import Response
from django.utils import timezone
from rest_framework import status
from django.http import Http404
from ctfidelidade.validators import *
from django.views.generic import TemplateView, ListView, CreateView
from django.urls import reverse_lazy
from ctfidelidade.forms import InsereRegistroForm
from .filters import ClienteFilter
from django.shortcuts import render

#
#	Registros
#

class RegistrosList(APIView):
	def get(self, request, format=None):
		registros = Registros.objects.all()
		serializer = RegistrosSerializer(registros, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = RegistrosSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# TODO - Separar a parte lógica da view

class RegistroDetail(APIView):
	serializer_class = RegistrosSerializer

	def get(self, request, cpf, format=None):
		registros = Registros.objects.filter(cliente__cpf = cpf)
		serializer = RegistrosSerializer(registros, many=True)
		return Response(serializer.data)

class IndexTemplateView(TemplateView):
    template_name = "ctfidelidade/index.html"

class RegistrosListView(ListView):
    template_name = "ctfidelidade/lista.html"
    model = Registros
    context_object_name = "registros"

class RegistroCreateView(CreateView):
    template_name = "ctfidelidade/cria.html"
    model = Registros
    form_class = InsereRegistroForm
    success_url = reverse_lazy("ctfidelidade:lista_registros")    

def busca(request):
 	clientes_list = Registros.objects.all()
 	cliente_filter = ClienteFilter(request.GET, queryset=clientes_list)
 	return render(request, 'ctfidelidade/busca.html', {'filter': cliente_filter})

def premios(request):
 	premios_list = Premios.objects.all()
 	premios_filter = ClienteFilter(request.GET, queryset=premios_list)
 	return render(request, 'ctfidelidade/premios.html', {'filter': premios_filter})
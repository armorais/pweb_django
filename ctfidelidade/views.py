from __future__ import unicode_literals
from ctfidelidade.models import *
from ctfidelidade.serializers import *
from rest_framework.views import  APIView
from rest_framework.response import Response
from django.utils import timezone
from rest_framework import status
from django.http import Http404
from django.views.generic import TemplateView, ListView, CreateView
from django.urls import reverse_lazy
from ctfidelidade.forms import InsereRegistroForm
from .filters import ClienteRegistroFilter, ClientePremioFilter
from django.shortcuts import render

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

class RegistroDetail(APIView):
	serializer_class = RegistrosSerializer

	def get(self, request, cpf, format=None):
		registros = Registros.objects.filter(cliente__cpf = cpf)
		serializer = RegistrosSerializer(registros, many=True)
		return Response(serializer.data)

class IndexTemplateView(TemplateView):
    template_name = "ctfidelidade/index.html"

class RegistrosListView(ListView):
    template_name = "ctfidelidade/lista_registros.html"
    model = Registros
    context_object_name = "registros"

class RegistroCreateView(CreateView):
    template_name = "ctfidelidade/cria.html"
    model = Registros
    form_class = InsereRegistroForm
    success_url = reverse_lazy("ctfidelidade:lista_registros")

# TO DO: quebrar o método em partes

    def validar_registros(self, cpf):
    	print(cpf)
    	registros = Registros.objects.filter(cliente__cpf = cpf).filter(status = True)
    	print(len(registros))
    	contador = 0
    	validos = {}
    	for aux in registros:
    		data_valida = aux.valido
    		servico = aux.servico
    		if (not data_valida):
    			aux.status = False
    			aux.save()
    		else:
    			if(servico.id not in validos):
    				validos[servico.id] = []
    			validos[servico.id].append(aux)
    			lista_validos = validos.get(servico.id)
    			if(len(lista_validos) >= servico.entradas):
    				for reg in lista_validos:
    			 		print(reg.data)
    			 		reg.status = False
    			 		reg.save()
    			 		print("premio gerado")
    				premio = Premios()
    				premio.baixado = False
    				premio.cliente = aux.cliente
    				premio.data = timezone.now()
    				premio.servico = aux.servico
    				premio.save()
    				break

    def form_valid(self, form):
	    """If the form is valid, save the associated model."""
	    self.object = form.save()
	    registro = self.object
	    cliente = registro.cliente
	    cpf = cliente.cpf
	    self.validar_registros(cpf)
	    premios_cliente = Premios.objects.filter(cliente__cpf = cpf)
	    return render(self.request, 'ctfidelidade/lista_premios.html', {'premios': premios_cliente})


def busca_registros(request):
 	registros_cliente_list = Registros.objects.all()
 	registros_cliente_filter = ClienteRegistroFilter(request.GET, queryset=registros_cliente_list)
 	return render(request, 'ctfidelidade/busca_registros.html', {'filter': registros_cliente_filter}) 	

def busca_premios(request):
 	premios_cliente_list = Premios.objects.all()
 	premios_cliente_filter = ClientePremioFilter(request.GET, queryset=premios_cliente_list)
 	return render(request, 'ctfidelidade/busca_premios.html', {'filter': premios_cliente_filter}) 
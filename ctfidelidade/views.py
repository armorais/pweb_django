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

    def validar_registros(self, cpf):
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
    		if((data_invalida == False) and (aux.status == True)):
    			contador+=1
    			validos.append(aux)
    			if (contador>=servico.entradas):
    				for reg in validos:
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
	    return render(self.request, 'ctfidelidade/premios.html', {'premios': premios_cliente})


def busca(request):
 	registros_cliente_list = Registros.objects.all()
 	registros_cliente_filter = ClienteFilter(request.GET, queryset=registros_cliente_list)
 	return render(request, 'ctfidelidade/busca.html', {'filter': registros_cliente_filter}) 	

def premios(request, cpf):
 	premios_list = Premios.objects.all()
 	premios_filter = ClienteFilter(request.GET, queryset=premios_list)
 	return render(request, 'ctfidelidade/premios.html', {'filter': premios_filter})
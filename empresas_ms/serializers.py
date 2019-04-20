from empresas_ms.models import Empresas
from rest_framework import serializers
from ctfidelidade.serializers import ServicosSerializer

class EmpresasSerializer(serializers.ModelSerializer):
	servicos = ServicosSerializer(many = True, read_only = True)

	class Meta:
		model = Empresas
		fields = ('cnpj', 'nome', 'servicos')
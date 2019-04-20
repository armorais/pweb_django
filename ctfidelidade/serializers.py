from ctfidelidade.models import *
from rest_framework import serializers

class ServicosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicos
        fields = ('descricao', 'validade', 'entradas', 'premio')

class RegistrosSerializer(serializers.ModelSerializer):
    cpf_cliente = serializers.CharField(source='cliente.cpf', read_only=True)
    nome_cliente = serializers.CharField(source='cliente.nome', read_only=True)
    nome_servico = serializers.CharField(source='servico', read_only=True)
    class Meta:
        model = Registros
        fields = ('data', 'nome_servico', 'cpf_cliente', 'nome_cliente', 'status')

class PremiosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Premios
        fields = ('data', 'servico', 'cliente', 'baixado')
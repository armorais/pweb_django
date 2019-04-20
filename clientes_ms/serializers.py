from clientes_ms.models import Clientes
from rest_framework import serializers

class ClientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clientes
        fields = ('cpf', 'nome', 'cep')
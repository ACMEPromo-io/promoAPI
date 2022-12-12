from Clientes.models import Clientes, ClientePromocao, Cupom
from rest_framework import serializers

class ClientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clientes
        fields = '__all__'

class ClientesPromocaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientePromocao
        fields = '__all__'

class CupomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cupom
        fields = '__all__'
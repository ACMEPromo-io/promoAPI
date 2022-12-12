from Clientes.models import Clientes, ClientePromocao, Cupoms
from rest_framework import serializers

class ClientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clientes
        fields = '__all__'

class ClientesPromocaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientePromocao
        fields = '__all__'

class CupomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cupoms
        fields = '__all__'
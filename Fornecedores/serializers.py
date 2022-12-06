from Fornecedores.models import Fornecedores
from rest_framework import serializers

class FornecedoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fornecedores
        fields = '__all__'

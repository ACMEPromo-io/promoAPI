from Aprovacoes.models import Aprovacoes
from rest_framework import serializers

class AprovacoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aprovacoes
        fields = '__all__'
from Promocoes.models import Promocoes
from rest_framework import serializers

class PromocoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promocoes
        fields = '__all__'

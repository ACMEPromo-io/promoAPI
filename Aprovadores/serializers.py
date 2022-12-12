from Aprovadores.models import Aprovadores
from rest_framework import serializers

class AprovadoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aprovadores
        fields = '__all__'
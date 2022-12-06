from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from Fornecedores.models import Fornecedores
from Fornecedores.serializers import FornecedoresSerializer

class FornecedoresViewSet(viewsets.ModelViewSet):
    serializer_class = FornecedoresSerializer
    queryset = Fornecedores.objects.all()


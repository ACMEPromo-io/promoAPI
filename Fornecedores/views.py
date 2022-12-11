from django.contrib.auth.models import User, Group
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework import permissions
from Fornecedores.models import Fornecedores
from Fornecedores.serializers import FornecedoresSerializer

class FornecedoresViewSet(viewsets.ModelViewSet):
    serializer_class = FornecedoresSerializer
    queryset = Fornecedores.objects.all()

      # including patch
    def patch(self, request, pk):
        fornecedor_object = self.get_object(pk)
        serializer = FornecedoresSerializer(fornecedor_object, data=request.data, partial=True) # set partial=True to update a data partially
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(code=201, data=serializer.data)
        return JsonResponse(code=400, data="wrong parameters")

    def delete(self, request, pk):
        fornecedor_object = self.get_object(pk)
        fornecedor_object.delete()
        return JsonResponse(code=200, data='')


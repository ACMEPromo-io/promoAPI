import time
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from Aprovacoes.models import Aprovacoes
from Aprovacoes.serializers import AprovacoesSerializer
from Aprovacoes.tasks import enqueueAprovacao

# Create your views here.
class AprovacoesViewSet(viewsets.ModelViewSet):
    serializer_class = AprovacoesSerializer
    queryset = Aprovacoes.objects.all()

    def create(self, request, *args, **kwargs):
        aprovacaoModel_object = Aprovacoes()
        serializer = AprovacoesSerializer(aprovacaoModel_object, data=request.data, partial=True) # set partial=True to update a data partially
        if serializer.is_valid():
            serializer.save()
            
            enqueueAprovacao.delay(serializer.data)
            return JsonResponse(data=serializer.data)
 
        return JsonResponse(data="wrong parameters", safe=False)

    # including patch
    def patch(self, request, pk):
        aprovacaoModel_object = self.get_object(pk)
        serializer = AprovacoesSerializer(aprovacaoModel_object, data=request.data, partial=True) # set partial=True to update a data partially
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data)
        return JsonResponse(data="wrong parameters")

    def delete(self, request, pk):
        aprovacaoModel_object = self.get_object(pk)
        aprovacaoModel_object.delete()
        return JsonResponse(data='')
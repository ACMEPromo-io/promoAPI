from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from Clientes.models import Clientes, ClientePromocao, Cupoms
from Clientes.serializers import ClientesSerializer, ClientesPromocaoSerializer, CupomsSerializer

# Create your views here.
class ClientesViewSet(viewsets.ModelViewSet):
    serializer_class = ClientesSerializer
    queryset = Clientes.objects.all()

    # including patch
    def patch(self, request, pk):
        clienteModel_object = self.get_object(pk)
        serializer = ClientesSerializer(clienteModel_object, data=request.data, partial=True) # set partial=True to update a data partially
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data)
        return JsonResponse(data="wrong parameters")

    def delete(self, request, pk):
        clienteModel_object = self.get_object(pk)
        clienteModel_object.delete()
        return JsonResponse(data='')

class ClientePromocaoViewSet(viewsets.ModelViewSet):
    serializer_class = ClientesPromocaoSerializer
    queryset = ClientePromocao.objects.all()

    def delete(self, request, pk):
        clientePromocaoModel_object = self.get_object(pk)
        clientePromocaoModel_object.delete()
        return JsonResponse(data='')

class CupomViewSet(viewsets.ModelViewSet):
    serializer_class = CupomsSerializer
    queryset = Cupoms.objects.all()

    def create(self, request, *args, **kwargs):
        cupomModel_object = Cupoms()
        novoCupom = request.data.dict()
        clienteCadastrado = ClientePromocao.objects.filter(idCliente = novoCupom['idCliente'], idPromocao = novoCupom['idPromocao'])
        if (len(clienteCadastrado) > 0):
            serializer = CupomsSerializer(cupomModel_object, data=request.data, partial=True) # set partial=True to update a data partially
            if serializer.is_valid():
                serializer.save()
            return JsonResponse(data=serializer.data)
 
        return JsonResponse(data="Cliente nao aceitou os termos da promocao", safe=False)

    # including patch
    def patch(self, request, pk):
        cupomModel_object = self.get_object(pk)
        serializer = CupomsSerializer(cupomModel_object, data=request.data, partial=True) # set partial=True to update a data partially
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data)
        return JsonResponse(data="wrong parameters")

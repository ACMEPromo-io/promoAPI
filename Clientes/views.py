from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from Clientes.models import Clientes, ClientePromocao, Cupom
from Clientes.serializers import ClientesSerializer, ClientesPromocaoSerializer, CupomSerializer

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
            return JsonResponse(code=201, data=serializer.data)
        return JsonResponse(code=400, data="wrong parameters")

    def delete(self, request, pk):
        clienteModel_object = self.get_object(pk)
        clienteModel_object.delete()
        return JsonResponse(code=200, data='')

class ClientePromocaoViewSet(viewsets.ModelViewSet):
    serializer_class = ClientesPromocaoSerializer
    queryset = ClientePromocao.objects.all()

    def delete(self, request, pk):
        clientePromocaoModel_object = self.get_object(pk)
        clientePromocaoModel_object.delete()
        return JsonResponse(code=200, data='')

class CupomViewSet(viewsets.ModelViewSet):
    serializer_class = CupomSerializer
    queryset = Cupom.objects.all()

    #def post(self, request):
        #cupomModel_object = Cupom()
        #print(request.data)
        #clienteCadastrado = ClientePromocao.objects.filter(idCliente = request.data.idCliente, idPromocao = request.data.idPromocao)
       
        #serializer = CupomSerializer(cupomModel_object, data=request.data, partial=True) # set partial=True to update a data partially

    # including patch
    def patch(self, request, pk):
        cupomModel_object = self.get_object(pk)
        serializer = CupomSerializer(cupomModel_object, data=request.data, partial=True) # set partial=True to update a data partially
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(code=201, data=serializer.data)
        return JsonResponse(code=400, data="wrong parameters")

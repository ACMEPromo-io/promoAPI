from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from Aprovadores.models import Aprovadores
from Aprovadores.serializers import AprovadoresSerializer

# Create your views here.
class AprovadoresViewSet(viewsets.ModelViewSet):
    serializer_class = AprovadoresSerializer
    queryset = Aprovadores.objects.all()

    # including patch
    def patch(self, request, pk):
        aprovadorModel_object = self.get_object(pk)
        serializer = AprovadoresSerializer(aprovadorModel_object, data=request.data, partial=True) # set partial=True to update a data partially
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(code=201, data=serializer.data)
        return JsonResponse(data="wrong parameters")
    
    def delete(self, request, pk):
        aprovadorModel_object = self.get_object(pk)
        aprovadorModel_object.delete()
        return JsonResponse(data='')
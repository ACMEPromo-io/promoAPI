from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from Promocoes.models import Promocoes
from Promocoes.serializers import PromocoesSerializer

# Create your views here.
class PromocoesViewSet(viewsets.ModelViewSet):
    serializer_class = PromocoesSerializer
    queryset = Promocoes.objects.all()

    # including patch
    def patch(self, request, pk):
        promocaoModel_object = self.get_object(pk)
        serializer = PromocoesSerializer(promocaoModel_object, data=request.data, partial=True) # set partial=True to update a data partially
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(code=201, data=serializer.data)
        return JsonResponse(code=400, data="wrong parameters")

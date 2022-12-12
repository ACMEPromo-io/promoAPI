import time
from celery import shared_task
from Aprovacoes.models import Aprovacoes
from Aprovacoes.serializers import AprovacoesSerializer

@shared_task
def enqueueAprovacao(aprovacao):
    aprovacaoModel_object = Aprovacoes()
    time.sleep(5)
    aprovacao['status'] = Aprovacoes.Status.APROVADO
    serializer = AprovacoesSerializer(aprovacaoModel_object, data=aprovacao, partial=True)

    if serializer.is_valid():
        serializer.save()
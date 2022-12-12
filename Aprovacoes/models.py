from django.db import models
from Aprovadores.models import Aprovadores
from Promocoes.models import Promocoes

# Create your models here.
class Aprovacoes(models.Model):

    class Status(models.TextChoices):
        PENDENTE = 'Pendente', 
        APROVADO = 'Aprovado', 
        RECUSADO = 'Recusado'
    
    idAprovacao = models.AutoField(primary_key=True)
    idAprovador = models.ForeignKey(Aprovadores, on_delete=models.CASCADE)
    idPromocao = models.ForeignKey(Promocoes, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDENTE)
    detalhes = models.CharField(max_length=500)
    dataAlteracao = models.DateField()
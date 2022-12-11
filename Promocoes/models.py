from django.db import models
from Fornecedores.models import Fornecedores

# Create your models here.
class Promocoes(models.Model):

    class Status(models.TextChoices):
        DRAFT = 'Rascunho', 
        APROVACAOPENDENTE = 'Aprovação Pendente', 
        APROVADO = 'Aprovado', 
        RECUSADO = 'Recusado', 
        ATIVO = 'Ativo', 
        FINALIZADO = 'Finalizado', 

    idPromocao = models.AutoField(primary_key=True)
    idFornecedor = models.ForeignKey(Fornecedores, on_delete=models.CASCADE)
    dataInicio = models.DateField()
    dataFim = models.DateField()
    quantidadeVencedores = models.IntegerField()
    maxCupomPessoa = models.IntegerField()
    valorCupom = models.FloatField()
    diasParaRecebimentoPremio = models.IntegerField()
    titulo = models.CharField(max_length=150)
    descricao = models.CharField(max_length=500)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.DRAFT)
    detalhesStatus = models.CharField(max_length=500)
    premio = models.CharField(max_length=150)
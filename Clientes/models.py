from django.db import models
from Promocoes.models import Promocoes

# Create your models here.
class Clientes(models.Model):
    idCliente = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=500)
    endereco = models.CharField(max_length=500)
    telefone = models.CharField(max_length=25)

class ClientePromocao(models.Model):
    idClientePromocao = models.AutoField(primary_key=True)
    idCliente = models.ForeignKey(Clientes, on_delete=models.DO_NOTHING)
    idPromocao = models.ForeignKey(Promocoes, on_delete=models.DO_NOTHING)

class Cupom(models.Model):

    class Status(models.TextChoices):
        VALIDO = 'Valido', 
        EXPIRADO = 'Expirado'

    idCupom = models.AutoField(primary_key=True)
    idPromocao = models.ForeignKey(Promocoes, on_delete=models.DO_NOTHING)
    idCliente = models.ForeignKey(Clientes, on_delete=models.DO_NOTHING)
    numeroCupom = models.IntegerField()
    dataDeCriacao = models.DateField()
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.VALIDO)
    sorteado = models.BooleanField()

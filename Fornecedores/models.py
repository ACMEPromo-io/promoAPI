from django.db import models

# Create your models here.
class Fornecedores(models.Model):
    idFornecedor = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=500)
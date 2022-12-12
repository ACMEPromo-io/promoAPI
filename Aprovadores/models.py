from django.db import models

# Create your models here.
class Aprovadores(models.Model):

    class Status(models.TextChoices):
        ACTIVE = 'Ativo', 
        DISMISSED = "Dispensado"

    idAprovador = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=500)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.ACTIVE)
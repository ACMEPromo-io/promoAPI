# Generated by Django 4.0.4 on 2022-12-11 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Promocoes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promocoes',
            name='status',
            field=models.CharField(choices=[('Rascunho', 'Draft'), ('Aprovação Pendente', 'Aprovacaopendente'), ('Aprovado', 'Aprovado'), ('Recusado', 'Recusado'), ('Ativo', 'Ativo'), ('Finalizado', 'Finalizado')], default='Rascunho', max_length=20),
        ),
    ]
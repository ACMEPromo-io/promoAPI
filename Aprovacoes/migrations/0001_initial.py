# Generated by Django 4.1.4 on 2022-12-12 00:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Aprovadores', '0001_initial'),
        ('Promocoes', '0002_alter_promocoes_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aprovacoes',
            fields=[
                ('idAprovacao', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('Aprovação Pendente', 'Aprovacaopendente'), ('Aprovado', 'Aprovado'), ('Recusado', 'Recusado')], default='Aprovação Pendente', max_length=20)),
                ('detalhes', models.CharField(max_length=500)),
                ('dataAlteracao', models.DateField()),
                ('idAprovador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Aprovadores.aprovadores')),
                ('idPromocao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Promocoes.promocoes')),
            ],
        ),
    ]

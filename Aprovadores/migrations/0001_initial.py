# Generated by Django 4.1.4 on 2022-12-11 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aprovadores',
            fields=[
                ('idAprovador', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=500)),
                ('status', models.CharField(choices=[('Ativo', 'Active'), ('Dispensado', 'Dismissed')], default='Ativo', max_length=20)),
            ],
        ),
    ]

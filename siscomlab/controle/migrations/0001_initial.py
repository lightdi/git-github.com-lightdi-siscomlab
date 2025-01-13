# Generated by Django 5.1.4 on 2025-01-13 02:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Laboratorio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255)),
                ('linhas', models.IntegerField()),
                ('colunas', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Maquina',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255)),
                ('laboratorio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='controle.laboratorio')),
            ],
        ),
    ]

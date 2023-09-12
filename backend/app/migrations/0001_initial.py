# Generated by Django 4.2.4 on 2023-09-12 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('nome', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('telefone', models.CharField(blank=True, max_length=20, null=True)),
                ('senha', models.CharField(blank=True, max_length=200, null=True)),
                ('cep', models.BigIntegerField(blank=True, null=True)),
                ('endereco', models.CharField(max_length=200)),
                ('rg', models.CharField(max_length=20)),
            ],
        ),
    ]

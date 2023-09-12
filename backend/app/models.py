from django.db import models

class Doador(models.Model):
    cpf = models.CharField(max_length=11, unique=True)
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    telefone = models.CharField(max_length=20, null=True, blank=True)
    senha = models.CharField(max_length=200, null=True, blank=True)
    cep = models.BigIntegerField(null=True, blank=True)
    endereco = models.CharField(max_length=200)
    rg = models.CharField(max_length=20)

    def __str__(self):
        return self.nome


# Create your models here.

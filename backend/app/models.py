from django.db import models

class Usuario(models.Model):
    data_nascimento = models.DateField ("Data de Nascimento")
    cpf = models.CharField("CPF", unique = True, max_length= 11)
    endereco = models.CharField(_"Endereço Completo", max_length=255)

class Doacao(models.Model):
    valor = models.DecimalField('Valor de doação', max_digits=10, decimal_places=2)
    confirmacao = models.BooleanField('Pagamento confirmado ?', default=False)


# Create your models here.

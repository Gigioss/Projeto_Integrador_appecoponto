from django.db import models

# Create your models here.
class Classes(models.Model):
    numero = models.CharField(default='-', max_length=15)
    CEP = models.CharField(default='-', max_length=15)
    BAIRRO = models.CharField(default='-', max_length=10)
    ENDERECO = models.CharField(default='-', max_length=15)
    SITUACAO = models.CharField(default='-', max_length=15)
    
class Usuario(models.Model):
    nome = models.CharField(default='-', max_length=15)
    cpf = models.CharField(default='-', max_length=15)
    email = models.CharField(default='-', max_length=10)
    ENDERECO = models.CharField(default='-', max_length=15)
    funcao = models.CharField(default='-', max_length=15)

class Descartadores(models.Model):
    nome = models.CharField(default='-', max_length=15)
    cpf = models.CharField(default='-', max_length=15)
    email = models.CharField(default='-', max_length=10)
    ENDERECO = models.CharField(default='-', max_length=15)

class Descarte(models.Model):
    nome = models.CharField(default='-', max_length=15)
    cpf = models.CharField(default='-', max_length=15)
    Ultimo_descarte = models.CharField(default='-', max_length=10)
    Proximo_descarte = models.CharField(default='-', max_length=15)
    


    

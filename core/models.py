from django.db import models

# Create your models here.

#criando entidade Pessoa (feito um tipo)
class Pessoa(models.Model):
    name = models.CharField('Nome completo',max_length=100)
    cpf = models.IntegerField('CPF',primary_key=True)
    email = models.EmailField('Email',null=True)

    #Usado para ajustar o plural
    class Meta:
        ordering = ['name']
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'
    #Retorna o nome
    def __str__(self):
        return self.name

class Cliente(models.Model):
    nome = models.CharField('Nome completo',max_length=100)
    nomeResumido = models.CharField("Nome resumido",max_length=50)
    cpf = models.IntegerField('CPF',primary_key=True)
    dataVencimento = models.DateField('Data de vencimento')

    #class Meta:
    #   ordering = ['nome']
    #  verbose_name = 'Cliente'
    #    verbose_name_plural 'Clientes'
    def __str__(self):
        return self.nome
from django.db import models

# Create your models here.

#criando entidade Pessoa (feito um tipo)
class Pessoa(models.Model):
    serie = models.CharField('Series',max_length=100)
    hobbie = models.CharField('Hobbies',max_length=100)
    emailContato = models.EmailField('Email',null=True)

    #Usado para ajustar o plural
    class Meta:
        ordering = ['serie']
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'
    #Retorna o nome
    def __str__(self):
        return self.serie

""" class Cliente(models.Model):
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

         """
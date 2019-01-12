from django.db import models
from atracoes.models import Atracao

class PontoTuristico(models.Model):
    #dados básicos
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)

    #lista de atrações
    atracoes = models.ManyToManyField(Atracao)

    def __str__(self):
        return self.nome
    
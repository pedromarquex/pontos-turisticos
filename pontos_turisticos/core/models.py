from django.db import models
from atracoes.models import Atracao
from comentarios.models import Comentario
from avaliacoes.models import Avaliacao

class PontoTuristico(models.Model):
    #dados básicos
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)

    #lista de atrações
    atracoes = models.ManyToManyField(Atracao)

    #comentarios sobre essa atração
    comentarios = models.ManyToManyField(Comentario)

    avaliacoes = models.ManyToManyField(Avaliacao)

    def __str__(self):
        return self.nome
    
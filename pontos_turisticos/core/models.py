from django.db import models
from atracoes.models import Atracao
from comentarios.models import Comentario
from avaliacoes.models import Avaliacao
from enderecos.models import Endereco

class PontoTuristico(models.Model):

    #dados básicos
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)

    #lista de atrações
    atracoes = models.ManyToManyField(Atracao)

    #comentarios sobre esse ponto turistico
    comentarios = models.ManyToManyField(Comentario)

    #avaliações sobre esse ponto turistico
    avaliacoes = models.ManyToManyField(Avaliacao)

    #endereço do ponto turistico
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)



    def __str__(self):
        return self.nome
    
from django.db import models

class PontoTuristico(models.Model):
    #dados básicos
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)

    def __str__(self):
        return self.nome
    
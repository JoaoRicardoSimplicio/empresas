from django.db import models


class Empresa(models.Model):

    comprador = models.CharField(max_length=110)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    quantidade = models.IntegerField()
    endereco = models.TextField()

    def __str__(self):
        return self.comprador

from django.db import models


class Relatorio(models.Model):

    nome = models.CharField(max_length=110, unique=True)
    total = models.DecimalField(max_digits=8, decimal_places=2, null=True)

    def __str__(self) -> str:
        return self.nome


class Empresa(models.Model):

    comprador = models.CharField(max_length=110)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    quantidade = models.IntegerField()
    endereco = models.TextField()
    relatorio = models.ForeignKey(Relatorio, related_name='empresas', on_delete=models.PROTECT, null=True)

    def delete(self) -> None:
        self.relatorio.total -= self.preco
        self.relatorio.save()
        super(Empresa, self).delete()

    def __str__(self) -> str:
        return self.comprador

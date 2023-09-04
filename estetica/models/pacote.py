from django.db import models

class Pacote(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0 )
    

    def __str__(self):
        return self.nome
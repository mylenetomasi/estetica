from django.db import models

class CadastroClientes (models.Model):
    descricao = models.CharField(max_length=100)



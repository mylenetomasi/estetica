from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=150)
    cpf = models.CharField(_("CPF"), max_length=11, blank=True, null=True)
    endereco = models.CharField (("endereço"), max_length=55,blank=True, null=False)
    telefone = models.CharField(_("telefone"), max_length=11, blank=True, null=True)
    email = models.EmailField(_("e-mail"), unique=True)
from django.db import models

from .cliente import Cliente
from .procedimento import Procedimento

class Agendamento(models.Model):
    Cliente = models.ForeignKey(Cliente,on_delete=models.PROTECT, null=False, related_name="Agendamento" )
    Procedimento = models.ForeignKey(Procedimento,on_delete=models.PROTECT, null=False, related_name="Agendamento")
    data_hora = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    confirmacao = models.CharField(max_length=100)

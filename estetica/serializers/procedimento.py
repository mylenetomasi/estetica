from rest_framework.serializers import ModelSerializer
from estetica.models import Procedimento

class ProcedimentoSerializer(ModelSerializer):
    class Meta:
        model = Procedimento
        fields= "__all__"

class ProcedimentoListSerializer(ModelSerializer):
    class Meta:
        model = Procedimento
        fields = ["id", "nome", "preco"]

class ProcedimentoDetailSerializer(ModelSerializer):
    class Meta:
        model = Procedimento
        fields = "__all__"
        depth = 1
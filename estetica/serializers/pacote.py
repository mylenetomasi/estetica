from rest_framework.serializers import ModelSerializer
from estetica.models import Pacote

class PacoteSerializer(ModelSerializer):
    class Meta:
        model = Pacote
        fields= "__all__"

class PacoteListSerializer(ModelSerializer):
    class Meta:
        model = Pacote
        fields = ["id", "nome", "status"]

class PacoteDetaiSerializer(ModelSerializer):
    class Meta:
        model = Pacote
        fields = "__all__"
        depth = 1
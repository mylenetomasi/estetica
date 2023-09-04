from rest_framework.serializers import ModelSerializer
from estetica.models import PacotesProcesso

class PacoteProcessoSerializer(ModelSerializer):
    class Meta:
        model = PacotesProcesso
        fields= "__all__"
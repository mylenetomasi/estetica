from rest_framework.serializers import ModelSerializer, SlugRelatedField, SerializerMethodField
from estetica.models import Pacote
from uploader.models import Image
from uploader.serializers import ImageSerializer

class PacoteSerializer(serializers.ModelSerializer):
    class Meta:
        imagem_attachment_key = serializers.SlugRelatedField(
            source="imagem",
            queryset=Image.objects.all(),
            slug_field="attachment_key",
            required=False,
            write_only=True,
        )
        imagem = ImageSerializer(required=False, read_only=True)
        model = Pacote
        fields= "__all__"

class PacoteListSerializer(serializers.ModelSerializer):
    class Meta:
        imagem = serializers.SerializerMethodField()
        model = Pacote
        fields = ["id", "nome", "status", "preco", "descricao"]

class PacoteDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pacote
        fields = "__all__"
        depth = 1

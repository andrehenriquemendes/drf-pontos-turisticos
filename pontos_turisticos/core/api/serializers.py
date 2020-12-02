from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristico
from atracoes.api.serializers import AtracaoSerializer
from comentarios.api.serializers import ComentarioSerializer
from enderecos.api.serializers import EnderecoSerializer


class PontoTuristicoSerializer(ModelSerializer):
    atracoes = AtracaoSerializer(many=True) # Traz a serializacao do modelo atracao
    comentarios = ComentarioSerializer(many=True) # many so usa se o relacionamento for many to many
    endereco = EnderecoSerializer()

    descricao_completa = SerializerMethodField() # incluindo informacoes adicionais

    class Meta:
        model = PontoTuristico
        fields = (
            'id', 'nome', 'descricao', 'aprovado', 'foto',
            'atracoes', 'comentarios', 'avaliacoes', 'endereco',
            'descricao_completa', 'descricao_completa2'
        )

    def get_descricao_completa(self, obj):
        return '%s - %s' % (obj.nome, obj.descricao)

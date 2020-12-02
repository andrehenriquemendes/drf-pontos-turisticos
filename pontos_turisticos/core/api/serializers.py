from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristico, DocIdentificacao
from atracoes.api.serializers import AtracaoSerializer
from comentarios.api.serializers import ComentarioSerializer
from enderecos.api.serializers import EnderecoSerializer
from atracoes.models import Atracao
from enderecos.models import Endereco

class DocIdentificacaoSerializer(ModelSerializer):
    class Meta:
        model = DocIdentificacao
        fields = '__all__'

class PontoTuristicoSerializer(ModelSerializer):
    atracoes = AtracaoSerializer(many=True) # Traz a serializacao do modelo atracao
    endereco = EnderecoSerializer() # many so usa se o relacionamento for many to many
    descricao_completa = SerializerMethodField() # incluindo informacoes adicionais
    doc_identificacao = DocIdentificacaoSerializer()

    class Meta:
        model = PontoTuristico
        fields = (
            'id', 'nome', 'descricao', 'aprovado', 'foto',
            'atracoes', 'comentarios', 'avaliacoes', 'endereco',
            'descricao_completa', 'descricao_completa2', 'doc_identificacao'
        )
        
        read_only_fields = ('comentarios', 'avaliacoes')

    def cria_atracoes(self, atracoes, ponto):
        # atrela as atracoes ao ponto turistico
        for atracao in atracoes:
            at = Atracao.objects.create(**atracao)
            ponto.atracoes.add(at)

    def create(self, validated_data):
        atracoes = validated_data['atracoes']
        del validated_data['atracoes']

        endereco = validated_data['endereco'] # obtem do post
        del validated_data['endereco'] # deleta

        doc = validated_data['doc_identificacao']
        del validated_data['doc_identificacao']
        doci = DocIdentificacao.objects.create(**doc)

        ponto = PontoTuristico.objects.create(**validated_data)
        self.cria_atracoes(atracoes, ponto)

        end = Endereco.objects.create(**endereco) # creia o endereco no BD
        ponto.endereco = end # atrela o endereco ao ponto
        ponto.doc_identificacao = doci

        ponto.save()

        return ponto

    def get_descricao_completa(self, obj):
        return '%s - %s' % (obj.nome, obj.descricao)

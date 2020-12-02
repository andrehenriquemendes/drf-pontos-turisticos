from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer

class PontoTuristicoViewSet(ModelViewSet):
    serializer_class = PontoTuristicoSerializer
    filter_backends = (SearchFilter,)
    permission_classes = (IsAuthenticated,) # seta as permissoes
    authentication_classes = (TokenAuthentication,) # qual a forma de autenticacao?
    search_fields = ('nome', 'descricao', 'endereco__linha1')
    # endereco eh chave estrangeira
    # linha1 eh um atributo do endereco
    lookup_field = 'id'
    # sobrescrevendo o metodo get_queryset
    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)
        queryset = PontoTuristico.objects.all()

        if id:
            queryset = PontoTuristico.objects.filter(pk=id)
        if nome:
            queryset = PontoTuristico.objects.filter(nome__iexact=nome)
        if descricao:
            queryset = PontoTuristico.objects.filter(descricao__iexact=descricao)
        
        return queryset

    def list(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).partial_update(request, *args, **kwargs)

    @action(methods=['get', 'post'], detail=True)
    def denunciar(self, request, pk=None):
        return Response({'method': pk})

    @action(methods=['get'], detail=True)
    def teste(self, request):
        pass

    @action(methods=['post'], detail=True)
    def associa_atracoes(self, request, id):
        atracoes = request.data['ids']

        ponto = PontoTuristico.objects.get(id=id)

        ponto.atracoes.set(atracoes)

        ponto.save()
        return HttpResponse('OK')

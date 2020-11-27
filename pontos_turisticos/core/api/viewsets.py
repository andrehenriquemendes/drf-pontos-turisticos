from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer
from rest_framework.response import Response

class PontoTuristicoViewSet(ModelViewSet):
    serializer_class = PontoTuristicoSerializer
    
    # sobrescrevendo o metodo get_queryset
    def get_queryset(self):
        return PontoTuristico.objects.filter(aprovado=True)

    def list(self, request, *args, **kwargs):
        return Response({'teste': 123})

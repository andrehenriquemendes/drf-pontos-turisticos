from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer

class PontoTuristicoViewSet(ModelViewSet):
    serializer_class = PontoTuristicoSerializer
    
    # sobrescrevendo o metodo get_queryset
    def get_queryset(self):
        return PontoTuristico.objects.filter(aprovado=True)

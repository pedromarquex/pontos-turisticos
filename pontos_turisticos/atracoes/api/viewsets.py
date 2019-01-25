from rest_framework.viewsets import ModelViewSet
from core.models import Atracao
from .serializers import AtracaoSerializer

class AtracaoViewSet(ModelViewSet):

    queryset = Atracao.objects.all()
    serializer_class = AtracaoSerializer
from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer

class PontoTuristicoViewSet(ModelViewSet):

    serializer_class = PontoTuristicoSerializer

    def get_queryset(self):
        return PontoTuristico.objects.filter(aprovado=True)

    # def list(self, request, *args, **kwargs):

        # é um metodo que é chamado quando o servidor recebe o verbo get
        # pode ser sobrescrito para alterar o comportamento da api
        #   pass

    #def create(self, request, *args, **kwargs):

        # é um metodo que é chamado quando o servidor recebe o verbo get
        # pode ser sobrescrito para alterar o comportamento da api
        #pass
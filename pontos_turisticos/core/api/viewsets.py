from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer
from rest_framework.decorators import action

class PontoTuristicoViewSet(ModelViewSet):

    serializer_class = PontoTuristicoSerializer

    # é a queryset que é executada quando o servidor recebe um get
    def get_queryset(self):
        return PontoTuristico.objects.filter(aprovado=True)

    # def list(self, request, *args, **kwargs):

        # é um metodo que é chamado quando o servidor recebe o verbo get
        # note que este get é para o endpoint como um todo
        # deve retornar uma lista de recursos
        # pode ser sobrescrito para alterar o comportamento da api
        # pass

    # def create(self, request, *args, **kwargs):

        # é um metodo que é chamado quando o servidor recebe o verbo post
        # pode ser sobrescrito para alterar o comportamento da api
        # pass

    # def destroy(self, request, *args, **kwargs):
        # é um metodo que é chamado quando o servidor recebe o verbo delete
        # pode ser sobrescrito para alterar o comportamento da api
        # não precisa passar o id do objeto para o método, pois o mesmo vai ser
        # passado em **kwargs nomeado, pondendo ser acessado por kwargs['pk']
        # pass

    # def retrieve(self, request, *args, **kwargs):
        # é um metodo que é chamado quando o servidor recebe o verbo get
        # note que este get é para o recurso
        # deve retornar um recurso como um todo
        # pode ser sobrescrito para alterar o comportamento da api
        # pass

    # def update(self, request, *args, **kwargs):
        # é um metodo que é chamado quando o servidor recebe o verbo put
        # deve alterar um objeto como um todo
        # pode ser sobrescrito para alterar o comportamento da api
        # pass

    # def partial_update(self, request, *args, **kwargs):
        # é um metodo que é chamado quando o servidor recebe o verbo patch
        # deve alterar um objeto como um todo
        # pode ser sobrescrito para alterar o comportamento da api
        # pass

    # @action()
    # recebe como parâmetro em qual método esta action será disparada
    # detail diz se a action é relativa ao endpoint ou a um recurso
    # detail=True manda a pk do recurso, False não
    @action(methods=['get'], detail=True)
    def denunciar(self, request, pk):
        pass

    @action(methods=['get'], detail=False)
    def teste(self, request):
        pass
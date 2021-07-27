from rest_framework import viewsets

from jogadores.models import jogadores
from jogadores.api.serializers import JogadoresSerializer

class JogadoresViewSet(viewsets.ModelViewSet):
    """ Exibir todos Jogadores """
    queryset = jogadores.objects.all()
    serializer_class = JogadoresSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']



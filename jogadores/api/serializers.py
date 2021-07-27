from rest_framework import serializers
from jogadores.models import jogadores

class JogadoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = jogadores
        fields = '__all__'
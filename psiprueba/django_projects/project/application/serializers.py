from .models import Canal, Usuario, Suscripcion
from rest_framework import serializers

class CanalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Canal
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class SuscripcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suscripcion
        fields = '__all__'
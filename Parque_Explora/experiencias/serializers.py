from rest_framework import serializers
from .models import ExperienciaInteractiva

class ExperienciaInteractivaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperienciaInteractiva
        fields = ['id', 'titulo', 'descripcion', 'sala_interactiva', 'imagen_relacionada_url', 'imagen']
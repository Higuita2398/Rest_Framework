# views.py

from rest_framework import generics, status
from rest_framework.response import Response
from .models import ExperienciaInteractiva
from .serializers import ExperienciaInteractivaSerializer

class ListaCrearExperienciaInteractiva(generics.ListCreateAPIView):
    queryset = ExperienciaInteractiva.objects.all()
    serializer_class = ExperienciaInteractivaSerializer

class DetalleActualizarEliminarExperienciaInteractiva(generics.RetrieveUpdateDestroyAPIView):
    queryset = ExperienciaInteractiva.objects.all()
    serializer_class = ExperienciaInteractivaSerializer
    
class ExperienciaInteractivaPorSala(generics.ListAPIView):
    serializer_class = ExperienciaInteractivaSerializer

    def get_queryset(self):
        nombre_sala = self.kwargs['nombre_sala']
        return ExperienciaInteractiva.objects.filter(sala_interactiva=nombre_sala)

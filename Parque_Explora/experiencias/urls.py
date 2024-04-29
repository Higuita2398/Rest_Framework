from django.urls import path
from . import views

urlpatterns = [
    path('experiencias/', views.ListaCrearExperienciaInteractiva.as_view(), name='lista-crear-experiencia'),
    path('experiencias/<int:pk>/', views.DetalleActualizarEliminarExperienciaInteractiva.as_view(), name='detalle-actualizar-eliminar-experiencia'),
    path('experiencias/salas/<str:nombre>/', views.ExperienciaInteractivaPorSala.as_view(), name='experiencia-por-sala'),
]

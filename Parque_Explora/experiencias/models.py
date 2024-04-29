from django.db import models
import requests

class ExperienciaInteractiva(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    sala_interactiva = models.CharField(max_length=100)
    imagen_relacionada_url = models.URLField()
    imagen = models.ImageField(upload_to='imagenes_interactivas/', blank=True, null=True)

    def save(self, *args, **kwargs):
        access_key = 'pvB6Yil1Un63AYmTFxNNqbSaflJxnqGrzEqlC9GQJAY'
        query = self.titulo

        # Realiza la solicitud a la API de Unsplash
        response = requests.get(
            f'https://api.unsplash.com/search/photos?query={query}',
            headers={'Authorization': f'Client-ID {access_key}'}
        )

        if response.status_code == 200:
            # Obtiene la URL de la primera imagen de la respuesta
            result = response.json()
            if result['total'] > 0:
                self.imagen_relacionada_url = result['results'][0]['urls']['regular']

        super(ExperienciaInteractiva, self).save(*args, **kwargs)
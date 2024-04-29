import os
import django

# Configurar las variables de entorno para Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Parque_Explora.settings")
django.setup()

# Importar el modelo de ExperienciaInteractiva después de configurar Django
from experiencias.models import ExperienciaInteractiva

# Función para inicializar la base de datos con datos dummy
def initialize_db_with_dummy_data():
    # Creamos algunas experiencias interactivas de ejemplo
    ExperienciaInteractiva.objects.create(
        titulo="Experiencia 1",
        descripcion="Descripción de la Experiencia 1",
        sala_interactiva="Sala 1"
    )

    ExperienciaInteractiva.objects.create(
        titulo="Experiencia 2",
        descripcion="Descripción de la Experiencia 2",
        sala_interactiva="Sala 2"
    )

    ExperienciaInteractiva.objects.create(
        titulo="Experiencia 3",
        descripcion="Descripción de la Experiencia 3",
        sala_interactiva="Sala 1"
    )

# Verifica si se está ejecutando este archivo directamente
if __name__ == "__main__":
    # Ejecuta la función de inicialización
    initialize_db_with_dummy_data()

import os
import sys
from django.apps import AppConfig

# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ClientsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.clients'

    def ready(self):
        if "runserver" in sys.argv or "shell" in sys.argv:
            from core import scheduler
            scheduler.iniciar()
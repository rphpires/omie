from django.apps import AppConfig


class ServiceOrderConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.service_order'

    verbose_name = 'Ordem de serviço'
    verbose_name_plural = 'Ordens de serviço'

    def ready(self):
        import apps.service_order.signals  # Registra os signals
from django.apps import AppConfig


class PurchaseOrderConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.purchase_order'

    verbose_name = 'Pedido de compra'
    verbose_name_plural = 'Pedidos de compra'
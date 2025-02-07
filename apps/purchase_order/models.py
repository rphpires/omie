from django.db import models


OPCOES = [
    ('N', 'Não'),
    ('S', 'Sim'),
]


class PurchaseStages(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)
    etapa = models.IntegerField(null=True, blank=True)
    gera_pendencia = models.CharField(max_length=1, choices=OPCOES, default='N')

    class Meta:
        db_table = 'purchase_order_stages'
        ordering = ['etapa']
        verbose_name = "Etapa"
        verbose_name_plural = "Etapas"
    

class PurchaseOrder(models.Model):
    id = models.IntegerField(primary_key=True)
    codigo_pedido = models.IntegerField(null=True, blank=True)  # codigo_pedido
    numero_pedido = models.IntegerField(null=True, blank=True)  # numero_pedido
    name = models.CharField(max_length=500, null=True, blank=True)
    projeto = models.ForeignKey('projects.Project', on_delete=models.PROTECT, related_name='pedidos', null=True, blank=True)
    etapa = models.ForeignKey(PurchaseStages, on_delete=models.SET_NULL, null=True, blank=True)
    client_id = models.ForeignKey('clients.Client', on_delete=models.PROTECT, related_name='pedidos', null=True, blank=True)
    data_previsao = models.DateField(null=True, blank=True)
    cancelado = models.CharField(max_length=1, choices=OPCOES, default='N')
    faturado = models.CharField(max_length=1, choices=OPCOES, default='N')
    pendencia = models.CharField(max_length=1, choices=OPCOES, default='N')

    #TODO: Fazer um app novo para os produtos e apenas relacionar aqui
    produto_codigo = models.CharField(max_length=500, null=True, blank=True)  # det["produto"]["codigo"]
    product_id = models.IntegerField(null=True, blank=True)  # det["produto"]["codigo_produto"]
    product_descricao = models.CharField(max_length=500, null=True, blank=True)  # det["produto"]["descricao"]
    product_quantidade = models.IntegerField(null=True, blank=True)  # det["produto"]["quantidade"]
    product_valor_unitario = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # det["produto"]["valor_unitario"]
    product_valor_total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # det["produto"]["valor_total"]

    @classmethod
    def calcular_total_por_pedido(cls):
        return cls.objects.values('codigo_pedido').annotate(
            total_pedido=models.Sum('product_valor_total')
        )

    class Meta:
        db_table = 'purchase_order'
        ordering = ['name']
        verbose_name = "Pedido de compra"
        verbose_name_plural = "Pedidos de compra"

    def __str__(self):
        return self.name
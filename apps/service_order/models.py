from django.db import models


OPCOES = [
    ('N', 'Não'),
    ('S', 'Sim'),
]


class ServiceStages(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)
    etapa = models.IntegerField(null=True, blank=True)
    gera_pendencia = models.CharField(max_length=1, choices=OPCOES, default='N')
    company =  models.ForeignKey("companies.Company", on_delete=models.PROTECT, related_name='services_stages', null=True, blank=True)
    
    class Meta:
        db_table = 'service_order_stages'
        ordering = ['etapa']
        verbose_name = "Etapa"
        verbose_name_plural = "Etapas"

    def __str__(self):
        return f"[{self.etapa}] {self.name}"


class ServiceOrder(models.Model):
    codigo_os = models.IntegerField(null=True, blank=True)  # codigo_pedido
    numero_os = models.IntegerField(null=True, blank=True)  # numero_pedido
    name = models.CharField(max_length=500, null=True, blank=True)
    etapa = models.ForeignKey(ServiceStages, on_delete=models.SET_NULL, null=True, blank=True)
    data_previsao = models.DateField(null=True, blank=True)
    cancelado = models.CharField(max_length=1, choices=OPCOES, default='N')
    faturado = models.CharField(max_length=1, choices=OPCOES, default='N')
    pendencia = models.CharField(max_length=1, choices=OPCOES, default='N')
    
    client = models.ForeignKey('clients.Client', on_delete=models.PROTECT, related_name='services', null=True, blank=True)
    projeto = models.ForeignKey('projects.Project', on_delete=models.PROTECT, related_name='services', null=True, blank=True)
    company =  models.ForeignKey("companies.Company", on_delete=models.PROTECT, related_name='services', null=True, blank=True)

    # temp_field = models.CharField(max_length=1, choices=OPCOES, default='N')
    #TODO: Fazer um app novo para os produtos e apenas relacionar aqui
    servico_id = models.IntegerField(null=True, blank=True)  # ServicosPrestados["nCodServico"]
    servico_item_id = models.IntegerField(null=True, blank=True)  # ServicosPrestados["nIdItem"]
    servico_descricao = models.CharField(max_length=500, null=True, blank=True)  # ServicosPrestados["cDescServ"]
    servico_quantidade = models.IntegerField(null=True, blank=True)  # ServicosPrestados["nQtde"]
    servico_valor_unitario = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # ServicosPrestados["nValUnit"]
    servico_valor_total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Cabecalho["nValorTotal"]

    @classmethod
    def calcular_total_por_servico(cls):
        return cls.objects.values('codigo_os').annotate(
            total_pedido=models.Sum('servico_valor_unitario')
        )

    class Meta:
        db_table = 'service_order'
        ordering = ['name']
        verbose_name = "Ordem de serviço"
        verbose_name_plural = "Ordens de serviço"


    def __str__(self):
        return f"{self.numero_os}, {self.name}"
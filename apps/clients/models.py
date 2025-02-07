from django.db import models
# from apps.companies.models import Company


class Client(models.Model):
    codigo_cliente = models.IntegerField(primary_key=True)
    razao_social = models.CharField(max_length=500, null=True, blank=True)
    nome_fantasia = models.CharField(max_length=500, null=True, blank=True)

    # temp_field = models.IntegerField(null=True, blank=True)
    company = models.ForeignKey("companies.Company", on_delete=models.PROTECT, related_name='client', null=True, blank=True)

    class Meta:
        db_table = 'clients'
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
    
    def __str__(self):
        return f"{self.razao_social or self.nome_fantasia}"
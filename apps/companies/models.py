from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField(null=True, blank=True)
    cnpj = models.CharField(max_length=20, null=True, blank=True)

    app_key = models.IntegerField(null=True, blank=True)
    app_secret = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'companies'
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

    def __str__(self):
        return f"{self.name}"
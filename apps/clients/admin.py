from django.contrib import admin

from .models import Client


@admin.register(Client)
class ClientsAdmin(admin.ModelAdmin):
    list_display = ["codigo_cliente", "razao_social", "nome_fantasia"]
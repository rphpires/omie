from django.contrib import admin

from .models import PurchaseStages, PurchaseOrder


@admin.register(PurchaseStages)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ["name", "etapa", "gera_pendencia"]


@admin.register(PurchaseOrder)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ["codigo_pedido", "name", "etapa"]
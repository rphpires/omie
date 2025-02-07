from django.contrib import admin

from .models import ServiceStages, ServiceOrder


@admin.register(ServiceStages)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ["name", "etapa", "gera_pendencia"]


@admin.register(ServiceOrder)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ["codigo_os", "numero_os", "name", "etapa", "projeto"]
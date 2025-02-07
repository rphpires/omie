from django.contrib import admin

from .models import Project
from apps.companies.models import Company

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ["project_id", "name"]
    search_fields = ('name',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "company":
            kwargs["queryset"] = Company.objects.order_by("name")  # Ordena as empresas pelo nome
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
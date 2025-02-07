# Generated by Django 5.1.5 on 2025-02-07 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_project_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='valor_pedidos_pendente',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='valor_servicos_pendente',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='valor_total_pedidos',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='valor_total_servicos',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
    ]

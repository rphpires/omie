# Generated by Django 5.1.5 on 2025-02-07 21:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
        ('service_order', '0003_remove_serviceorder_temp_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicestages',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='services_stages', to='companies.company'),
        ),
    ]

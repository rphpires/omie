# Generated by Django 5.1.5 on 2025-02-07 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviceorder',
            name='temp_field',
            field=models.CharField(choices=[('N', 'Não'), ('S', 'Sim')], default='N', max_length=1),
        ),
    ]

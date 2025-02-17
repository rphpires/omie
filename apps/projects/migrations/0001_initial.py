# Generated by Django 5.1.5 on 2025-02-07 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('project_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=500)),
                ('inativo', models.CharField(choices=[('N', 'Não'), ('S', 'Sim')], default='N', max_length=1)),
                ('info_created_at', models.DateTimeField(blank=True, null=True)),
                ('info_updated_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('temp_field', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Projeto',
                'verbose_name_plural': 'Projetos',
                'db_table': 'projects',
                'ordering': ['project_id', 'name'],
            },
        ),
    ]

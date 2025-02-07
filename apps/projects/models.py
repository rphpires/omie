from django.db import models


OPCOES = [
    ('N', 'Não'),
    ('S', 'Sim'),
]


class Project(models.Model):
    project_id = models.IntegerField(primary_key=True)  # codigo
    name = models.CharField(max_length=500)  # nome
    inativo = models.CharField(max_length=1, choices=OPCOES, default='N')

    info_created_at = models.DateTimeField(null=True, blank=True)  # info["data_inc"] + info["hora_inc"]
    info_updated_at = models.DateTimeField(null=True, blank=True)  # info["data_alt"] + info["hora_alt"]

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    company = models.ForeignKey("companies.Company", on_delete=models.PROTECT, related_name='projects', null=True, blank=True)

    class Meta:
        db_table = 'projects'
        ordering = ['project_id', 'name']
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'

    def __str__(self):
        return f"<Project> {self.project_id}_{self.name}"
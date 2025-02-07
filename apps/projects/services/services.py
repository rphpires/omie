from django.db import transaction
from .functions import *

from ..models import Project
from apps.companies.models import Company

from libs.global_functions import *
from libs.omie_api import OmieConnection


def projects_import():
    trace("Updating Omie projects")
    try:
        companies = Company.objects.values('id', 'name', 'app_key', 'app_secret')
        for company in companies:
            try:
                trace(f"Handling company: {company['name']}")
                omie = OmieConnection(company['app_key'], company['app_secret'])

                ret = omie.listar_projetos()  # Suponha que ret seja uma lista de dicionários
                trace(f"Received data: {ret}")

                if not ret:
                    trace(f"No clients found for {company['name']}")
                    continue
                
                company_instance = Company.objects.get(id=company['id'])

                # Inserindo ou atualizando os clientes no banco de dados
                with transaction.atomic():  # Garante que todas as operações sejam atômicas
                    for pr in ret:
                        client, created = Project.objects.update_or_create(
                            project_id=pr.get("codigo"),  # ID único do Omie
                            defaults={
                                "name": pr.get("nome"),
                                "inativo": pr.get("inativo"),
                                "info_created_at": format_date_time(pr["info"].get("data_inc"), pr["info"].get("hora_inc")),
                                "info_updated_at": format_date_time(pr["info"].get("data_alt"), pr["info"].get("hora_alt")),
                                "company": company_instance
                            }
                        )
                        action = "Created" if created else "Updated"
                        trace(f"{action} client: {client.name}")

                trace("Omie clients update finished")
            
            except Exception as ex:
                report_exception(ex)
 
    except Exception as ex:
        report_exception(ex)
            
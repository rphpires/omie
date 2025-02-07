from django.db import transaction

from ..models import Client
from apps.companies.models import Company

from libs.global_functions import *
from libs.omie_api import OmieConnection


def clients_import():
    trace("Updating Omie clients")

    companies = Company.objects.values('id', 'name', 'app_key', 'app_secret')
    for company in companies:
        trace(f"Handling company: {company['name']}")
        omie = OmieConnection(company['app_key'], company['app_secret'])

        ret = omie.listar_clientes()  # Suponha que ret seja uma lista de dicionários
        trace(f"Received data: {ret}")

        if not ret:
            trace(f"No clients found for {company['name']}")
            continue

        # Inserindo ou atualizando os clientes no banco de dados
        with transaction.atomic():  # Garante que todas as operações sejam atômicas
            for client_data in ret:
                client, created = Client.objects.update_or_create(
                    codigo_cliente=client_data.get("codigo_cliente"),  # ID único do Omie
                    defaults={
                        "razao_social": client_data.get("razao_social"),
                        "nome_fantasia": client_data.get("nome_fantasia"),
                        "company_id": company['id'],  # Associa o cliente à empresa correspondente
                    }
                )
                action = "Created" if created else "Updated"
                trace(f"{action} client: {client.nome_fantasia or client.razao_social}")

        trace("Omie clients update finished")
        

    
    
    

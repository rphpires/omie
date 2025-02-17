from django.db import transaction
from .functions import *

from ..models import ServiceOrder, ServiceStages
from apps.companies.models import Company
from apps.projects.models import Project
from apps.clients.models import Client

from libs.global_functions import *
from libs.omie_api import OmieConnection


def servicos_import():
    trace("Atualizando as Ordens de serviço")
    companies = Company.objects.values('id', 'name', 'app_key', 'app_secret')
    for company in companies:
        try:
            trace(f"Handling company: {company['name']}")
            omie = OmieConnection(company['app_key'], company['app_secret'])

            trace(f"## Antes da requisição")
            ret = omie.listar_ordem_servicos()
            trace(f"Received data: {ret}")

            if not ret:
                trace(f"No clients found for {company['name']}")
                continue
            
            company_instance = Company.objects.get(id=company['id'])
            
            # Inserindo ou atualizando os clientes no banco de dados
            with transaction.atomic():  # Garante que todas as operações sejam atômicas
                for os in ret:
                    try:
                        cabecalho = os["Cabecalho"]
                        info_cadastro = os["InfoCadastro"]
                        servicos_prestados = os["ServicosPrestados"]
                        trace(f"Criando lista de serviços prestados: total={len(servicos_prestados)}")

                        stage = ServiceStages.objects.filter(etapa=cabecalho.get("cEtapa"), company=company_instance).first()
                        project_instance = Project.objects.filter(project_id=os["InformacoesAdicionais"].get("nCodProj")).first()
                        client_instance = Client.objects.filter(codigo_cliente=cabecalho.get("nCodCli")).first()

                        for serv in servicos_prestados:
                            ordem_de_servico, created = ServiceOrder.objects.update_or_create(
                                codigo_os=cabecalho.get("nCodOS"),  # ID único do Omie
                                defaults={
                                    "numero_os": cabecalho.get("cNumOS"),
                                    "projeto": project_instance,
                                    "client_id": client_instance,
                                    "company": company_instance, 
                                    "etapa": stage,
                                    "data_previsao": convert_date(cabecalho.get("dDtPrevisao")),
                                    "cancelado": info_cadastro.get("cCancelada"),
                                    "servico_id": serv.get("nCodServico"),
                                    "servico_item_id": serv.get("nIdItem"),
                                    "servico_descricao": serv.get("cDescServ"),
                                    "servico_quantidade": serv.get("nQtde"),
                                    "servico_valor_unitario": serv.get("nValUnit"),
                                    "servico_valor_total": cabecalho.get("nValorTotal"),
                                }
                            )
                            action = "Created" if created else "Updated"
                            trace(f"{action} os: {ordem_de_servico.numero_os}, {ordem_de_servico.projeto}")
                    
                    except Exception as ex:
                        report_exception(ex)
            
            trace("Omie clients update finished")
            
        except Exception as ex:
            report_exception(ex)
    
    
    

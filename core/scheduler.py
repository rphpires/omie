# scheduler.py
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore
from datetime import datetime
from functools import wraps

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from datetime import datetime

from libs.global_functions import *

from apps.clients.services.services import clients_import
from apps.service_order.services.services import servicos_import
from apps.projects.services.services import projects_import
from apps.purchase_order.services import pedidos_import



def log_execucao(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Iniciando {func.__name__} em {datetime.now()}")
        result = func(*args, **kwargs)
        print(f"Finalizando {func.__name__} em {datetime.now()}")
        return result
    return wrapper


@log_execucao
def funcao_app1():
    trace(f"App1 executado em: {datetime.now()}")
    # clients_import()
    servicos_import()
    # projects_import()
    funcao_app2()


@log_execucao
def funcao_app2():
    print(f"App2 executado em: {datetime.now()}")
    funcao_app3()


@log_execucao
def funcao_app3():
    print(f"App3 executado em: {datetime.now()}")


def iniciar():
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), "default")
    
    # Agende apenas a primeira função
    scheduler.add_job(
        funcao_app1,
        trigger=CronTrigger(minute=0),  # Executa apenas no minuto 0 de cada hora
        name="tarefa_horas_cheias"
    )
    
    scheduler.start()
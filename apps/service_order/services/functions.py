from datetime import datetime
from libs.global_functions import *


def convert_date(date_str):
    """Converte uma data de 'DD/MM/YYYY' para 'YYYY-MM-DD'."""
    try:
        return datetime.strptime(date_str, "%d/%m/%Y").strftime("%Y-%m-%d")
    except ValueError:
        return None  # Retorna None se o formato estiver inválido

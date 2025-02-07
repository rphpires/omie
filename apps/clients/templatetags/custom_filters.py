import json
from django import template

register = template.Library()

@register.filter
def split_first(value, arg='_'):
    """Divida a string com base no separador (default '_') e retorne a primeira parte"""
    if isinstance(value, str):
        return value.split(arg)[0]
    return value  # Retorna o valor original caso não seja uma string


@register.filter
def format_percentage(value):
    """Formata o valor como porcentagem com 2 casas decimais."""
    try:
        return "{:.2f}%".format(value)
    except (TypeError, ValueError):
        return value  # Retorna o valor original caso haja erro

@register.filter
def format_number(value):
    """Formata o número com vírgula para separar milhar e com 2 casas decimais."""
    try:
        return "{:,.2f}".format(value)
    except (TypeError, ValueError):
        return value  # Retorna o valor original caso haja erro

@register.filter
def to_json(value):
    return json.dumps(value)

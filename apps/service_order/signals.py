from django.db.models.signals import post_save
from django.db.models import Sum
from django.dispatch import receiver
from .models import ServiceOrder

from apps.projects.models import Project


@receiver(post_save, sender=ServiceOrder)
def atualizar_valor_total(sender, instance, **kwargs):
    # A instância de ServiceOrder foi salva ou atualizada
    print('###### Signal')
    # Obtém o projeto associado ao ServiceOrder
    projeto = instance.projeto

    if projeto:
        # Soma o valor total de todos os ServiceOrders associados a este projeto
        valor_total_servicos = ServiceOrder.objects.filter(projeto=projeto).aggregate(Sum('servico_valor_total'))['servico_valor_total__sum'] or 0

        print(f'Valor total serviços: {valor_total_servicos}')
        # Atualiza o campo valor_total no modelo Project
        projeto.valor_total_servicos = valor_total_servicos
        projeto.save()

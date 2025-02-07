import json
import os
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import threading

from core.scheduler import funcao_app1


def read_json(filename):
    print(os.path.abspath(f'apps/clients/aux_files/{filename}.json'))
    with open(f'apps/clients/aux_files/{filename}.json', 'r') as file:
        return json.load(file)

def index(request):
    sorted_data = read_json('complete_final_obj')
    metrics_data = read_json('complete_final_sum_count')
    return render(request, 'index.html', {
        'data': sorted_data,
        'metrics': metrics_data
    })


def index(request):
    sorted_data = read_json('complete_final_obj')
    metrics_data = read_json('complete_final_sum_count')

    # Agrupando os dados por CNPJ
    grouped_data = {}
    for key, item in sorted_data.items():
        cnpj = item['cnpj']
        if cnpj not in grouped_data:
            grouped_data[cnpj] = []
        grouped_data[cnpj].append((key, item))

    # Ordenando os itens dentro de cada grupo pela pendência
    for cnpj in grouped_data:
        grouped_data[cnpj] = sorted(grouped_data[cnpj], key=lambda x: x[1]['pendencia'], reverse=True)

    return render(
        request, 
        'index.html', 
        {
            'grouped_data': grouped_data,
            'metrics': metrics_data
        }
    )


@csrf_exempt
def executar_tarefa(request):
    if request.method == "POST":
        # Executa a função em uma thread separada para evitar bloqueio da requisição
        thread = threading.Thread(target=funcao_app1)
        thread.start()

        return JsonResponse({"mensagem": "Execução manual iniciada com sucesso!"})
    
    return JsonResponse({"erro": "Método não permitido"}, status=405)
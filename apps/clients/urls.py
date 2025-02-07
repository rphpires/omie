from django.urls import path
from .views import executar_tarefa, index

urlpatterns = [
    path('', index, name='index'),
    path("executar-tarefa", executar_tarefa, name="executar_tarefa"),
]
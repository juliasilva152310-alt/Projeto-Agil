import time
import heapq

# Estrutura de tarefa com prioridade
class Tarefa:
    def __init__(self, nome, prioridade):
        self.nome = nome
        self.prioridade = prioridade  # menor número = mais crítico

    def __lt__(self, outra):
        return self.prioridade < outra.prioridade

# Lista de tarefas (fila de prioridade)
tarefas = []
heapq.heappush(tarefas, Tarefa("Corrigir bug no sistema", 1))
heapq.heappush(tarefas, Tarefa("Revisar relatório", 3))
heapq.heappush(tarefas, Tarefa("Atualizar documentação", 5))

# Monitoramento em tempo real
while tarefas:
    tarefa = heapq.heappop(tarefas)
    print(f"Executando tarefa crítica: {tarefa.nome} (prioridade {tarefa.prioridade})")
    time.sleep(2)  # simula tempo de execução
    print(f"Tarefa concluída: {tarefa.nome}\n")

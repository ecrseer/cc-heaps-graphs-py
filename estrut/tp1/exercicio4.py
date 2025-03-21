class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, item):
        # Adiciona o elemento ao final e ajusta o heap para cima
        self.heap.append(item)
        self._heapify_up(len(self.heap) - 1)

    def pop(self):
        # Remove o elemento de menor prioridade (raiz)
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        # Move o último elemento para a raiz e ajusta o heap para baixo
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def _heapify_up(self, index):
        # Ajusta o heap para cima
        parent_index = (index - 1) // 2
        while index > 0 and self.heap[index][0] < self.heap[parent_index][0]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index
            parent_index = (index - 1) // 2

    def _heapify_down(self, index):
        # Ajusta o heap para baixo
        smallest = index
        left_child = 2 * index + 1  # 2i + 1
        right_child = 2 * index + 2  # 2i + 2

        if left_child < len(self.heap) and self.heap[left_child][0] < self.heap[smallest][0]:
            smallest = left_child
        if right_child < len(self.heap) and self.heap[right_child][0] < self.heap[smallest][0]:
            smallest = right_child

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)


# Lista de tarefas com prioridades
tarefas = [(3, 'Tarefa A'), (1, 'Tarefa B'), (2, 'Tarefa C'), (4, 'Tarefa D'), (6, 'Tarefa E'), (5, 'Tarefa F')]

# Criação do MinHeap e inserção das tarefas
heap = MinHeap()
for tarefa in tarefas:
    heap.insert(tarefa)

# Extração e execução das tarefas em ordem de prioridade
while len(heap.heap) > 0:
    prioridade, tarefa = heap.pop()
    print(f"Executando {tarefa} com prioridade {prioridade}")

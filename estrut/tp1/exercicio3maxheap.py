class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, item):
        # Adiciona o elemento ao final e ajusta o heap para cima
        self.heap.append(item)
        self._heapify_up(len(self.heap) - 1)

    def pop(self):
        # Remove e retorna o maior elemento (raiz)
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
        # Ajusta o heap para cima, mantendo a propriedade de MaxHeap
        parent_index = (index - 1) // 2
        while index > 0 and self.heap[index] > self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index
            parent_index = (index - 1) // 2

    def _heapify_down(self, index):
        # Ajusta o heap para baixo, mantendo a propriedade de MaxHeap
        largest = index
        left_child = 2 * index + 1  # 2i + 1
        right_child = 2 * index + 2 # 2i + 2

        # Verifica se o filho esquerdo é maior que o nó atual
        if left_child < len(self.heap) and self.heap[left_child] > self.heap[largest]:
            largest = left_child

        # Verifica se o filho direito é maior que o nó atual
        if right_child < len(self.heap) and self.heap[right_child] > self.heap[largest]:
            largest = right_child

        # Se o maior valor não for o nó atual, faz a troca e continua o ajuste
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)

    def peek(self):
        # Retorna o maior elemento (raiz) sem removê-lo
        if len(self.heap) > 0:
            return self.heap[0]
        return None

    def size(self):
        # Retorna o tamanho do heap
        return len(self.heap)

    def is_empty(self):
        # Verifica se o heap está vazio
        return len(self.heap) == 0


# Exemplo de uso da MaxHeap
heap = MaxHeap()

# Inserindo elementos
heap.insert(50)
heap.insert(30)
heap.insert(40)
heap.insert(10)
heap.insert(20)
heap.insert(35)
heap.insert(45)


# Verificando o maior elemento
print(f"Maior elemento: {heap.peek()}")  # Saída: 30
sorteado=heap.pop()
print(f"Removido: {sorteado}")

opa=heap.pop()
print(f"Removido: {opa}")
# Removendo elementos em ordem decrescente
while not heap.is_empty():
    print(f"Removido: {heap.pop()}")

import time
import matplotlib.pyplot as plt
import random

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
        while index > 0 and self.heap[index] < self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index
            parent_index = (index - 1) // 2

    def _heapify_down(self, index):
        # Ajusta o heap para baixo
        smallest = index
        left_child = 2 * index + 1  # 2i + 1
        right_child = 2 * index + 2  # 2i + 2

        if left_child < len(self.heap) and self.heap[left_child] < self.heap[smallest]:
            smallest = left_child
        if right_child < len(self.heap) and self.heap[right_child] < self.heap[smallest]:
            smallest = right_child

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

    def para_heap_binaria(self, items):
        self.heap = items
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self._heapify_down(i)

    def display_heap(self):
        return self.heap


def duracao_heap(size):


    lista = random.sample(range(size * 2), size)

    # Criação e medição do tempo da heap
    heap = MinHeap()
    start_time = time.time()
    heap.para_heap_binaria(lista)
    end_time = time.time()

    return end_time - start_time, lista[-3:]  # Retorna tempo e os 3 últimos valores da lista


def exercicio11():
    # Tamanhos diferentes de heaps
    sizes = [100, 1000, 10000]
    tempos = []
    ultimos_valores = []

    # Medir o tempo de construção da heap para cada tamanho
    for size in sizes:
        tempo, valores = duracao_heap(size)
        tempos.append(tempo * 1000)  # Convertendo para milissegundos
        ultimos_valores.append(valores)

    # Printando o tempo e os 3 últimos valores de cada lista
    for i, size in enumerate(sizes):
        print(f"Tamanho da lista: {size}")
        print(f"Tempo de construção (ms): {tempos[i]:.4f}")
        print(f"Últimos 3 valores da lista: {ultimos_valores[i]}")
        print("-" * 40)

    plot_this(sizes, tempos)


# Plotando os tempos de construção para diferentes tamanhos
def plot_this(percursos, tempos):
    plt.figure(figsize=(8, 5))
    plt.plot(percursos, tempos, marker='o', linestyle='-', color='b')
    plt.xlabel("Tamanho da Heap")
    plt.ylabel("Tempo total (ms)")
    plt.title("Tempos de Construção de Heap para Diferentes Tamanhos")
    plt.grid()
    plt.show()

exercicio11()



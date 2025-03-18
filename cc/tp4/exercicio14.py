import time
import random
import matplotlib.pyplot as plt


class MinHeap:
    def __init__(self):
        self.heap = []

    def inserir(self, item):
        self.heap.append(item)
        self._heapify_up(len(self.heap) - 1)

    def pop(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        while index > 0 and self.heap[index] < self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index
            parent_index = (index - 1) // 2

    def _heapify_down(self, index):
        smallest = index
        left_child = 2 * index + 1
        right_child = 2 * index + 2

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

    def exibir_heap(self):
        return self.heap

    def remover_raiz(self):
        if len(self.heap) == 0:
            return None
        root = self.heap[0]
        # Troca a raiz com o último elemento
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root


def medir_duracao_remocao(size):
    lista = random.sample(range(size * 2), size)
    heap = MinHeap()
    heap.para_heap_binaria(lista)

    # Estado da heap antes da remoção
    estado_inicial = heap.exibir_heap()

    start_time = time.time()
    raiz_removida = heap.remover_raiz()
    end_time = time.time()

    # Estado da heap após a remoção
    estado_final = heap.exibir_heap()

    return end_time - start_time, estado_inicial, estado_final


def exercicio14():
    sizes = [1000, 25000, 500000, 1000000]
    tempos = []
    estados_iniciais = []
    estados_finais = []

    for size in sizes:
        tempo, estado_inicial, estado_final = medir_duracao_remocao(size)
        tempos.append(tempo * 1000)  # Convertendo para milissegundos
        estados_iniciais.append(estado_inicial)
        estados_finais.append(estado_final)

    for i, size in enumerate(sizes):
        print(f"Tamanho da lista: {size}")
        print(f"Tempo de remoção (ms): {tempos[i]:.4f}")
        print("-" * 40)

    plot_this(sizes, tempos)


def plot_this(percursos, tempos):
    plt.figure(figsize=(8, 5))
    plt.plot(percursos, tempos, marker='o', linestyle='-', color='b')
    plt.xlabel("Tamanho da Heap")
    plt.ylabel("Tempo de Remoção (ms)")
    plt.title("Tempos de Remoção da Raiz em uma Min-Heap")
    plt.grid()
    plt.show()


exercicio14()

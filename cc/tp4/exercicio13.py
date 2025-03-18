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

    def buscar(self, valor):
        for elemento in self.heap:
            if elemento == valor:
                return True
        return False


def medir_duracao_busca(size, valor_buscar):
    lista = random.sample(range(size * 2), size)
    heap = MinHeap()
    heap.para_heap_binaria(lista)
    start_time = time.time()
    resultado = heap.buscar(valor_buscar)
    end_time = time.time()

    return end_time - start_time, resultado


def exercicio13():
    sizes = [100, 1000, 10000]
    tempos = []
    resultados = []
    valor_buscar = 25

    for size in sizes:
        tempo, resultado = medir_duracao_busca(size, valor_buscar)
        tempos.append(tempo * 1000)
        resultados.append(resultado)

    for i, size in enumerate(sizes):
        print(f"Tamanho da lista: {size}")
        print(f"Tempo de busca (ms): {tempos[i]:.4f}")
        print(f"Resultado da busca: {'Encontrado' if resultados[i] else 'Não encontrado'}")
        print("-" * 40)

    plot_this(sizes, tempos)


def plot_this(percursos, tempos):
    plt.figure(figsize=(8, 5))
    plt.plot(percursos, tempos, marker='o', linestyle='-', color='b')
    plt.xlabel("Tamanho da Heap")
    plt.ylabel("Tempo de Busca (ms)")
    plt.title("Tempos de Busca na Heap para Diferentes Tamanhos")
    plt.grid()
    plt.show()


exercicio13()

class MinHeap:
    def __init__(self):
        self.heap = []

    def inserir(self, item):
        self.heap.append(item)
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, indice):
        pai = (indice - 1) // 2
        if pai >= 0 and self.heap[indice] < self.heap[pai]:
            self.heap[pai], self.heap[indice] = self.heap[indice], self.heap[pai]
            self.heapify_up(pai)

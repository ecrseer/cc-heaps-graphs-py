class MinHeap:
    def __init__(self):
        self.heap = []

    def _heapify(self, indice, tamanho):
        """Ajusta o heap para manter a propriedade do heap mínimo"""
        menor = indice
        esq = 2 * indice + 1
        dir = 2 * indice + 2

        if esq < tamanho and self.heap[esq][1] < self.heap[menor][1]:
            menor = esq
        if dir < tamanho and self.heap[dir][1] < self.heap[menor][1]:
            menor = dir

        if menor != indice:
            self.heap[indice], self.heap[menor] = self.heap[menor], self.heap[indice]
            self._heapify(menor, tamanho)

    def inserir(self, nome, prioridade):
        """Insere um novo elemento na fila de prioridade"""
        self.heap.append((nome, prioridade))
        indice = len(self.heap) - 1


        while indice > 0:
            pai = (indice - 1) // 2
            if self.heap[indice][1] < self.heap[pai][1]:
                self.heap[indice], self.heap[pai] = self.heap[pai], self.heap[indice]
                indice = pai
            else:
                break

    def remover(self):
        """Remove o item de menor prioridade da fila"""
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()


        raiz = self.heap[0]
        self.heap[0] = self.heap.pop()


        self._heapify(0, len(self.heap))

        return raiz



def solicitar_dados():
    fila = MinHeap()
    fila.inserir('Amanda - febre', 2)
    fila.inserir('Bruno - dor de cabeça', 1)
    fila.inserir('Eduarda - sangramento', 5)
    fila.inserir('Carla - dor nas costas', 3)
    fila.inserir('Daniel - dor de garganta', 1)


    paciente = fila.remover()
    while paciente is not  None:
        print(f"Próximo paciente: {paciente[0]} - prioridade {paciente[1]}")
        paciente = fila.remover()

    print("Fila de prioridade vazia.")



if __name__ == "__main__":
    solicitar_dados()

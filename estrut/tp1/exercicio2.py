class MinHeap:
    def __init__(self):
        self.heap = []

    def _heapify(self, indice, tamanho):
        """Ajusta o heap para manter a propriedade do heap mínimo"""
        menor = indice
        esq = 2 * indice + 1  # Filho esquerdo
        dir = 2 * indice + 2  # Filho direito

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

        # Ajusta o heap para manter a propriedade do heap mínimo
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

        # O item de menor prioridade está na raiz (índice 0)
        raiz = self.heap[0]
        self.heap[0] = self.heap.pop()

        # Reajusta o heap após remover o item
        self._heapify(0, len(self.heap))

        return raiz


# Função para solicitar os dados ao usuário
def solicitar_dados():
    fila = MinHeap()
    fila.inserir('Amanda - febre', 2)
    fila.inserir('Bruno - dor de cabeça', 1)
    fila.inserir('Eduarda - sangramento', 5)
    fila.inserir('Carla - dor nas costas', 3)
    fila.inserir('Daniel - dor de garganta', 1)
    for paciente in fila.heap:
        print(f"Próximo paciente: {paciente[0]} - prioridade {paciente[1]}")


if __name__ == "__main__":
    solicitar_dados()

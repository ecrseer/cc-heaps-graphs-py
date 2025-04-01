class MinHeap:
    def __init__(self):
        self.heap = []

    def _heapify_up(self, index):
        """Ajusta o heap para cima."""
        parent_index = (index - 1) // 2
        while index > 0 and self.heap[index][1] < self.heap[parent_index][1]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index
            parent_index = (index - 1) // 2

    def _heapify_down(self, index):
        """Ajusta o heap para baixo"""
        smallest = index
        left_child = 2 * index + 1
        right_child = 2 * index + 2

        if left_child < len(self.heap) and self.heap[left_child][1] < self.heap[smallest][1]:
            smallest = left_child

        if right_child < len(self.heap) and self.heap[right_child][1] < self.heap[smallest][1]:
            smallest = right_child

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

    def inserir(self, nome, prioridade):
        """Insere um novo elemento na fila de prioridade."""
        self.heap.append((nome, prioridade))
        self._heapify_up(len(self.heap) - 1)

    def remover(self):
        """Remove o item de menor prioridade da fila."""
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        raiz = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)

        return raiz

    def modificar_processo(self, nome_processo, nova_prioridade):
        """Modifica a prioridade de um processo na fila."""
        for i in range(len(self.heap)):
            if self.heap[i][0] == nome_processo:
                prioridade_antiga = self.heap[i][1]
                self.heap[i] = (nome_processo, nova_prioridade)

                if nova_prioridade < prioridade_antiga:
                    self._heapify_up(i)
                else:
                    self._heapify_down(i)
                return

    def esta_vazia(self):
        """Verifica se a fila de prioridade está vazia"""
        return len(self.heap) == 0

    def ordenar(self):
        """Ordena todos os elementos da fila de prioridade"""
        resultado = []
        while not self.esta_vazia():
            resultado.append(self.remover())
        return resultado

    def mostrar(self, ctx):
        for item in self.heap:
            print(f"Processo: {item[0]}, Prioridade: {item[1]}")


def iniciar():
    processos = MinHeap()
    processos.inserir('Google Chrome', 7)
    processos.inserir('Spotify', 4)
    processos.inserir('Discord', 5)
    processos.inserir('Visual Studio Code', 3)
    processos.inserir('Zoom', 1)
    processos.inserir('Telegram', 3)
    processos.inserir('WhatsApp', 7)
    processos.inserir('Slack', 4)

    opcao_selecionada = mostrar_opcoes()
    executar = {
        "1": inserir_processo,
        "2": executar_proximo_processo,
        "3": altera_processo,
        "4": processos.mostrar,
        "sair": lambda x: print("Saindo do programa.")
    }

    while opcao_selecionada != "sair":
        executar[opcao_selecionada](processos)
        opcao_selecionada = mostrar_opcoes()


def altera_processo(fila):
    nome_processo = input("Digite o nome do processo que deseja modificar: ")
    nova_prioridade = int(input("Digite a nova prioridade do processo: "))
    fila.modificar_processo(nome_processo, nova_prioridade)


def executar_proximo_processo(fila):
    if fila.esta_vazia():
        print("A fila de prioridade está vazia.")
        return

    nome, prioridade = fila.remover()
    print(f"Executando {nome} com prioridade {prioridade}")


def inserir_processo(fila):
    nome = input("Digite o nome do processo: ")
    prioridade = int(input("Digite a prioridade do processo: "))
    fila.inserir(nome, prioridade)


def mostrar_opcoes():
    return input("""
    Escolha uma opção:
    1 - Inserir um novo processo na Heap
    2 - Executar o proximo processo na Heap
    3 - Modificar a prioridade do processo na Heap
    4 - Mostrar fila de processos
    sair - Sair do programa
    """)


# Garantir que o código seja executado corretamente no terminal
if __name__ == "__main__":
    iniciar()

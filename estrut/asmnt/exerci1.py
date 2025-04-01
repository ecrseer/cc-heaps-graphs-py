class MinHeap:
    def __init__(self):
        self.heap = []

    def _heapify(self, indice, tamanho):
        """Ajusta o heap para manter a propriedade do heap mínimo"""
        menor = indice
        filho_esq = 2 * indice + 1
        filho_direito = 2 * indice + 2

        if filho_esq < tamanho and self.heap[filho_esq][1] < self.heap[menor][1]:
            menor = filho_esq
        if filho_direito < tamanho and self.heap[filho_direito][1] < self.heap[menor][1]:
            menor = filho_direito

        if menor != indice:
            self.heap[indice], self.heap[menor] = self.heap[menor], self.heap[indice]
            self._heapify(menor, tamanho)

    def inserir(self, nome, prioridade):
        """Insere um novo elemento na fila de prioridade"""
        self.heap.append((nome, prioridade))
        indice = len(self.heap) - 1

        # desce arvore e troca se prioridade filho < prioridade pai
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

    def esta_vazia(self):
        """Verifica se a fila de prioridade está vazia"""
        return len(self.heap) == 0

    def ordenar(self):
        """Ordena todos os elementos da fila de prioridade"""
        resultado = []
        while not self.esta_vazia():
            resultado.append(self.remover())
        return resultado

    def mostrar(self,ctx):
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
        "3": modificar_processo,
        "4": processos.mostrar,
        "sair": lambda x: print("Saindo do programa.")
    }

    while opcao_selecionada != "sair":
        executar[opcao_selecionada](processos)
        opcao_selecionada = mostrar_opcoes()



def modificar_processo(fila):
    nome_processo = input("Digite o nome do processo que deseja modificar: ")
    for i in range(len(fila.heap)):
        if fila.heap[i][0] == nome_processo:
            nova_prioridade = int(input(f"Digite a nova prioridade de {nome_processo}: "))
            fila.heap[i] = (nome_processo, nova_prioridade)
            fila._heapify(i, len(fila.heap))
            print(f"Processo {nome_processo} modificado com sucesso.")
            print(f"heap após: {fila.heap}")
            return


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

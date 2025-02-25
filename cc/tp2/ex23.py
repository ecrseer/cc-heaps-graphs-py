class QuickSelect:
    def qckSelect(self, lista, low, high, k):
        # Caso base: se o array tiver apenas um elemento
        if low == high:
            return lista[low]

        # Particiona o array e obtém o índice do pivô
        pivot_index = self._partition(lista, low, high)

        # Caso em que o pivô é o k-ésimo menor elemento
        if k == pivot_index:
            return lista[k]
        # Caso o k-ési11mo elemento esteja à esquerda do pivô
        elif k < pivot_index:
            return self.qckSelect(lista, low, pivot_index - 1, k)
        # Caso o k-ésimo elemento esteja à direita do pivô
        else:
            return self.qckSelect(lista, pivot_index + 1, high, k)

    def _partition(self, lista, low, high):
        # Escolhe o pivô como o último elemento
        pivot = lista[high]
        i = low - 1  # Índice do menor elemento

        for j in range(low, high):
            # Se o elemento atual for menor ou igual ao pivô
            if lista[j] <= pivot:
                i += 1
                lista[i], lista[j] = lista[j], lista[i]  # Troca os elementos

        # Coloca o pivô na posição correta
        lista[i + 1], lista[high] = lista[high], lista[i + 1]

        return i + 1


def encontrar_kesimo_menor_elemento(array, k):
    return QuickSelect().qckSelect(array, 0, len(array) - 1, k - 1)  # k - 1 porque o índice é zero-based

def demonstracao(array,k):
    print(f"\n---\nDado a lista {array} e k = {k}")
    result = encontrar_kesimo_menor_elemento(array, k)
    print(f"ordenada: {sorted(array)}")
    print(f"O {k}-ésimo menor elemento é: {result}")

def exercicio23():
    print("Exercício 2.3: Quick Select")
    lista_um = [10, 4, 5, 8, 6, 11, 26, 30, 35, 12, 14]
    k1 = 7

    lista_dois = [4,2,3,5,1,5,2]
    k2 = 3

    lista_tres = [55,1,32,42,3,2,7,99,22,31,45,23,12,11,1]
    k3 = 4

    lista_quatro = [32,51,6,2,7,11,12,13,16,17,18]
    k4 = 5

    demonstracao(lista_um,k1)
    demonstracao(lista_dois,k2)
    demonstracao(lista_tres,k3)
    demonstracao(lista_quatro,k4)

    lista_cinco = [42,23,12,11,1,2,3,7,22,31,45,55,99]
    k5 = 2

    lista_seis = [18,17,7,6,2,51,32]
    k6 = 1

    lista_sete = [1,3,7, 1,32,42,12,23,35,55,99]
    k7 = 8

    lista_oito  = [9,8,7,6,5,4,3,2,1]
    k8 = 5

    demonstracao(lista_cinco,k5)
    demonstracao(lista_seis,k6)
    demonstracao(lista_sete,k7)
    demonstracao(lista_oito,k8)

    lista_nove = [1,2,3,4,5,6,7,8,9]
    k9 = 8

    lista_dez = [99,3,52]
    k10 = 2

    demonstracao(lista_nove,k9)
    demonstracao(lista_dez,k10)





if __name__ == '__main__':
    exercicio23()
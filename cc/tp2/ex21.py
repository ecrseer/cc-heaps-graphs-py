import time
import matplotlib.pyplot as plt


class QuickSort:
    primeiro_pivo = -1

    def __init__(self, primeiro_pivo=-1):
        self.primeiro_pivo = primeiro_pivo

    def ordenar_quick_sort(self, lista_desordenada):
        inicio = time.time()
        lista_ordenada = self.quick_sort_completo(lista_desordenada)
        tempo_total = time.time() - inicio
        return lista_ordenada, tempo_total

    def quick_sort_completo(self, lista):
        if len(lista) <= 1:
            return lista
        elif self.primeiro_pivo != -1:
            pivo = self.primeiro_pivo
            self.primeiro_pivo = -1
        else:
            pivo = lista.pop()

        menores, maiores = [], []
        for item in lista:
            if item < pivo:
                menores.append(item)
            else:
                maiores.append(item)

        return self.quick_sort_completo(menores) + [pivo] + self.quick_sort_completo(maiores)


def plot_this(concurrency_levels, times):
    plt.figure(figsize=(8, 5))
    plt.plot(concurrency_levels, times, marker='o', linestyle='-')
    plt.xlabel("Pivo")
    plt.ylabel("Tempo total (ms)")
    plt.title("Exercicio 21 Ordenacao Quick Sort pivo")
    plt.grid()
    plt.show()


def exercicio21():
    numeros = [3, 6, 8, 10, 4, 32, 5, 1, 2, 1]
    pivo_inicio = QuickSort(primeiro_pivo=0).ordenar_quick_sort(numeros)
    meio = len(numeros) // 2
    pivo_meio = QuickSort(primeiro_pivo=meio).ordenar_quick_sort(numeros)

    fim = len(numeros) - 1
    pivo_fim = QuickSort(primeiro_pivo=fim).ordenar_quick_sort(numeros)
    plot_this(["No inicio", "No meio", "No fim"], [pivo_inicio[1], pivo_meio[1], pivo_fim[1]])


if __name__ == '__main__':
    exercicio21()

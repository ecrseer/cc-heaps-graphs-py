import time
import matplotlib.pyplot as plt


class QuickSort:
    def ordenar_quick_sort(self, lista_desordenada):
        inicio = time.time()
        lista_ordenada = self.quick_sort_completo(lista_desordenada)
        tempo_total = time.time() - inicio
        return lista_ordenada, tempo_total

    def quick_sort_completo(self, lista):
        if len(lista) <= 1:
            return lista
        else:
            pivo = lista.pop()

        menores, maiores = [], []
        for item in lista:
            if item['nota'] < pivo['nota']:
                menores.append(item)
            else:
                maiores.append(item)

        return self.quick_sort_completo(menores) + [pivo] + self.quick_sort_completo(maiores)


def exercicio22():
    estudantes = [{"nome": "Gabriel", "nota": 10}, {"nome": "Maria", "nota": 8}, {"nome": "João", "nota": 6},
                  {"nome": "José", "nota": 4}, {"nome": "Ana", "nota": 2}]
    ordenados,tempo=QuickSort().ordenar_quick_sort(estudantes)
    print(f"Ordenados: {ordenados}")


if __name__ == '__main__':
    exercicio22()

import time
import numpy as np
from concurrent.futures import ProcessPoolExecutor
import os
import matplotlib.pyplot as plt

def multiplicacao_linha(linha):
    return np.dot(linha, matrizB_global)

def multiplicacao_sequencial(matrizA, matrizB):
    return np.dot(matrizA, matrizB)

def multiplicacao_paralela(matrizA, matrizB, num_workers=None):
    global matrizB_global
    matrizB_global = matrizB

    if num_workers is None:
        num_workers = os.cpu_count()

    with ProcessPoolExecutor(max_workers=num_workers) as executor:
        resultado = list(executor.map(multiplicacao_linha, matrizA))

    return np.array(resultado)

def cria_matriz_tamanho(tamanho):
    return np.random.randint(1, 100, size=(tamanho, tamanho))

def exercicio_22():
    tamanhos_matriz = [50, 100, 200, 500, 1000, 2000]
    tempos_seq = []
    tempos_par = []

    for tamanho in tamanhos_matriz:
        matrizA = cria_matriz_tamanho(tamanho)
        matrizB = cria_matriz_tamanho(tamanho)

        inicio = time.time()
        multiplicacao_sequencial(matrizA, matrizB)
        tempo_seq = time.time() - inicio
        tempos_seq.append(tempo_seq)
        print(f"duracao sequencial para tamanho {tamanho}: {tempo_seq:.12f}s")

        inicio = time.time()
        multiplicacao_paralela(matrizA, matrizB)
        tempo_par = time.time() - inicio
        tempos_par.append(tempo_par)
        print(f"duracao paralela para tamanho {tamanho}: {tempo_par:.12f}s")

    plot_this(tamanhos_matriz, tempos_seq, tempos_par)

def plot_this(tamanhos_matriz, tempos_seq, tempos_par):
    plt.figure(figsize=(8, 5))
    plt.plot(tamanhos_matriz, tempos_seq, marker='o', linestyle='-', color='b', label="Sequencial")
    plt.plot(tamanhos_matriz, tempos_par, marker='o', linestyle='-', color='r', label="Paralela")
    plt.xlabel("Tamanho da Matriz")
    plt.ylabel("Tempo (segundos)")
    plt.title("Comparação de Tempo entre Multiplicação Sequencial e Paralela")
    plt.legend()
    plt.grid()
    plt.show()

exercicio_22()

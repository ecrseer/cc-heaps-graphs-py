import random
import time
from concurrent.futures import ProcessPoolExecutor
import os
import matplotlib.pyplot as plt

def soma_sequencial(lista):
    return sum(lista)

def soma_paralela(lista, num_workers=None):
    if num_workers is None:
        num_workers = os.cpu_count()
    tamanho_pedaco = len(lista) // num_workers
    partes_por_threads = [lista[i * tamanho_pedaco: (i + 1) * tamanho_pedaco] for i in range(num_workers)]

    with ProcessPoolExecutor(max_workers=num_workers) as executor:
        somas_parciais = list(executor.map(soma_sequencial, partes_por_threads))

    return sum(somas_parciais)

def cria_lista_grande():
    dezMilhoes = 10 ** 7 
    lista_teste = list(range(1, dezMilhoes + 1))
    return lista_teste

def exercicio_21():
    dezMilhoes_lista_teste = cria_lista_grande()
 
    tamanho_lista = [10**6, 10**7]
    tempos_seq = []
    tempos_par = []

    for tamanho in tamanho_lista:
        dezMilhoes_lista_teste = list(range(1, tamanho + 1))

        inicio = time.time()
        soma_sequencial(dezMilhoes_lista_teste)
        tempo_seq = time.time() - inicio
        print(f"duracao sequencial ({tempo_seq:.12f}s)")
        tempos_seq.append(tempo_seq)

        inicio = time.time()
        soma_paralela(dezMilhoes_lista_teste)
        tempo_par = time.time() - inicio
        print(f"duracao paralela ({tempo_par:.12f}s)")
        tempos_par.append(tempo_par)
    
    plot_this(tamanho_lista, tempos_seq, tempos_par)

def plot_this(tamanho_lista, tempos_seq, tempos_par):
    plt.figure(figsize=(8, 5))
    plt.plot(tamanho_lista, tempos_seq, marker='o', linestyle='-', color='b', label="Sequencial")
    plt.plot(tamanho_lista, tempos_par, marker='o', linestyle='-', color='r', label="Paralela")
    plt.xlabel("Tamanho da Lista")
    plt.ylabel("Tempo (segundos)")
    plt.title("Comparação de Tempo entre Soma Sequencial e Paralela")
    plt.legend()
    plt.grid()
    plt.show()

exercicio_21()

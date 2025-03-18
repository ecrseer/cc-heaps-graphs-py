import time
import os
import matplotlib.pyplot as plt
from concurrent.futures import ProcessPoolExecutor

def verifica_primo(numero):
    if numero < 2:
        return False
    if numero in (2, 3):
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

def contar_primos_sequencial(intervalo):
    return sum(1 for numero in intervalo if verifica_primo(numero))

def contar_primos_paralelo(intervalo, num_workers=None):
    if num_workers is None:
        num_workers = os.cpu_count()
    
    tamanho_pedaco = len(intervalo) // num_workers
    partes = [intervalo[i * tamanho_pedaco:(i + 1) * tamanho_pedaco] for i in range(num_workers)]

    with ProcessPoolExecutor(max_workers=num_workers) as executor:
        contagens_parciais = executor.map(contar_primos_sequencial, partes)

    return sum(contagens_parciais)

def exercicio_primos():
    limites_superiores = [10**4, 5*10**4, 10**5]
    tempos_seq = []
    tempos_par = []

    for limite in limites_superiores:
        intervalo = list(range(1, limite + 1))

        inicio = time.time()
        contar_primos_sequencial(intervalo)
        tempo_seq = time.time() - inicio
        print(f"duracao sequencial para {limite}: {tempo_seq:.6f}s")
        tempos_seq.append(tempo_seq)

        inicio = time.time()
        contar_primos_paralelo(intervalo)
        tempo_par = time.time() - inicio
        print(f"duracao paralela para {limite}: {tempo_par:.6f}s")
        tempos_par.append(tempo_par)

    plot_this(limites_superiores, tempos_seq, tempos_par)

def plot_this(intervalos, tempos_seq, tempos_par):
    plt.figure(figsize=(8, 5))
    plt.plot(intervalos, tempos_seq, marker='o', linestyle='-', color='b', label="Sequencial")
    plt.plot(intervalos, tempos_par, marker='o', linestyle='-', color='r', label="Paralela")
    plt.xlabel("Intervalo Analisado")
    plt.ylabel("Tempo (segundos)")
    plt.title("Comparação de Tempo: Contagem de Primos")
    plt.legend()
    plt.grid()
    plt.show()

exercicio_primos()

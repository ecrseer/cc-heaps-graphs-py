import random
import time
from concurrent.futures import ProcessPoolExecutor

def max_sequencial(lista):
    return max(lista)



def max_paralelo(lista, num_workers=4):
    tamanho_pedaco = len(lista) // num_workers
    partes = [lista[i * tamanho_pedaco: (i + 1) * tamanho_pedaco] for i in range(num_workers)]

    with ProcessPoolExecutor(max_workers=num_workers) as executor:
        maximos_parciais = list(executor.map(max_sequencial, partes))

    return max(maximos_parciais)

def cria_lista_grande():
    N = 10 ** 6
    lista_teste = [random.randint(0, 10 ** 6) for _ in range(N)]
    return lista_teste


def exercicio_54():
    lista_teste = cria_lista_grande()
    inicio = time.time()
    resultado_seq = max_sequencial(lista_teste)
    tempo_seq = time.time() - inicio
    inicio = time.time()
    resultado_par = max_paralelo(lista_teste)
    tempo_par = time.time() - inicio
    print(f"Máximo encontrado (Sequencial): {resultado_seq} em {tempo_seq:.6f} segundos")
    print(f"Máximo encontrado (Paralelo): {resultado_par} em {tempo_par:.6f} segundos")


exercicio_54()

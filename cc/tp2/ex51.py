import time
from multiprocessing import Pool

def somar_paralel(lst):
    with Pool() as pool:
        chunk_size = len(lst) // 4
        chunks = [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]
        results = pool.map(sum, chunks)
    return sum(results)

large_list = list(range(1, 10001))

inicio = time.time()
soma_paralela = somar_paralel(large_list)
tempo_soma_para = time.time() - inicio
print(f"Soma paralela: {tempo_soma_para:.10f} milissegundos")



inicio2 = time.time()
soma_sequencial = sum(large_list)
tempo_soma_seque = time.time() - inicio2

print(f"Soma sequencial, Tempo: {tempo_soma_seque:.10f} milissegundos")

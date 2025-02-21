from multiprocessing import Pool
import random

from vector import somar_vet_aleatorio
from vector import vector_by_scalar;

def sum_chunk(chunk):
    return sum(chunk)

def oldex12():
    data = [random.randint(1, 100000) for _ in range(10000)]
    chunks = [data[i:i + 1000] for i in range(0, len(data), 1000)]

    with Pool() as pool:
        result = sum(pool.map(sum_chunk, chunks))
    print(f"Soma total: {result}")
    aa=sum([12,3])
    print(aa)
    dd=vector_by_scalar(data)
    print(dd)

def ex12():
    vet,soma=somar_vet_aleatorio()
    print(f"Vetor: {vet}")
    print(f"Soma: {soma}")


if __name__ == '__main__':
    ex12()



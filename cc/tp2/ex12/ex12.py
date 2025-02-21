import time

from vector import somar_vet_aleatorio,somar_vet_linear;



def ex12():
    print("Exercício 1.2: Cálculo Paralelo com OpenMP (simulação com multiprocessing)")
    print("Somando vetor aleatório")
    inicio = time.time()
    soma=somar_vet_aleatorio()
    # print(f"Vetor: {vet}")
    print(f"Soma: {soma}")
    demorou = time.time() - inicio
    print(f"Demorou {demorou:.2f} segundos")

    print("\n---\nSomando vetor linear")
    inicio = time.time()
    soma = somar_vet_linear()
    # print(f"Vetor: {vet2}")
    print(f"Soma: {soma}")
    demorou = time.time() - inicio
    print(f"Demorou {demorou:.2f} segundos")


if __name__ == '__main__':
    ex12()



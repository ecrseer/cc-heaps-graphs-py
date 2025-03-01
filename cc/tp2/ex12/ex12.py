import time

from vector import somar_vet_aleatorio, somar_vet_linear;


def realizar_somas():
    print("Somando vetor aleatório")
    inicio = time.time()
    soma = somar_vet_aleatorio()
    demorou_aleatorio = time.time() - inicio

    print("\n---\nSomando vetor linear")
    inicio_linear = time.time()
    soma_linear = somar_vet_linear()
    demorou_linear = time.time() - inicio_linear
    return demorou_aleatorio, demorou_linear


def ex12():
    aleatorio_media = 0
    linear_media = 0
    for i in range(10):
        aleatorio_ms, linear_ms = realizar_somas()
        aleatorio_media += aleatorio_ms
        linear_media += linear_ms

    aleatorio_media /= 10
    linear_media /= 10
    print(f"\nMédia de tempo para somar vetor aleatório: {aleatorio_media:.2f} milisegundos")
    print(f"Média de tempo para somar vetor linear: {linear_media:.2f} milisegundos")


if __name__ == '__main__':
    ex12()

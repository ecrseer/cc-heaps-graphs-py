import time

from matplotlib import pyplot as plt


def hanoi_transfere(n, inicio, chegada, aux):
    if n == 1:
        print("Mova o disco 1 do destino", inicio, "para ", chegada)
        return
    hanoi_transfere(n - 1, inicio, aux, chegada)
    print("Mova o disco", n, "do destino", inicio, "para ", chegada)
    hanoi_transfere(n - 1, aux, chegada, inicio)


def measure_time(func, n):
    start = time.time()
    func(n, 'A', 'C', 'B')

    end = time.time()
    return end - start


def plot_this(tempos):
    plt.figure(figsize=(10, 5))
    plt.plot(range(5, 15), tempos, 'b-', label="Hanoi (Recursive)")
    plt.xlabel("Numero de Discos(N)")
    plt.ylabel("Tempo (segundos)")
    plt.legend()
    plt.title("Torre de Hanoi")
    plt.show()


hanoi_times = []
for n in range(5, 15):
    hanoi_times.append(measure_time(hanoi_transfere, n))

plot_this(hanoi_times)

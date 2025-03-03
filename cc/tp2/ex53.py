import random
import time
import multiprocessing
import matplotlib.pyplot as plt


def merge_sort_sequencial(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort_sequencial(arr[:mid])
    right = merge_sort_sequencial(arr[mid:])
    return merge(left, right)


def merge(left, right):
    sorted_arr = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    return sorted_arr



def mergesort_paralelo(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_part = arr[:mid]
    right_part = arr[mid:]

    with multiprocessing.Pool(processes=2) as pool:
        left_sorted, right_sorted = pool.map(merge_sort_sequencial, [left_part, right_part])

    return merge(left_sorted, right_sorted)


# Medir tempo de execução
def measure_time(sort_function, arr):
    start = time.time()
    sorted_arr = sort_function(arr)
    return time.time() - start, sorted_arr


if __name__ == "__main__":
    sizes = [2**i for i in range(10, 18)]  # Tamanhos de 1024 até 131072
    sequential_times = []
    parallel_times = []

    for size in sizes:
        arr = [random.randint(0, 100000) for _ in range(size)]

        seq_time, _ = measure_time(merge_sort_sequencial, arr)
        par_time, _ = measure_time(mergesort_paralelo, arr)

        sequential_times.append(seq_time)
        parallel_times.append(par_time)

        print(f"Tamanho: {size} | Sequencial: {seq_time:.6f}s | Paralelo: {par_time:.6f}s")


    plt.figure(figsize=(8, 10))
    plt.plot(sizes, sequential_times, 'r-o', label="MergeSort Sequencial")
    plt.plot(sizes, parallel_times, 'b-o', label="MergeSort Paralelo")
    plt.xlabel("Tamanho da Lista")
    plt.ylabel("Tempo (ms)")
    plt.title("Comparação MergeSort: Sequencial vs Paralelo")
    plt.legend()
    plt.grid()
    plt.show()

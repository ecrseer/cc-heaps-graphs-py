import time
import random
from concurrent.futures import ProcessPoolExecutor
import matplotlib.pyplot as plt



class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self._insert(current.left, value)
        else:
            if current.right is None:
                current.right = Node(value)
            else:
                self._insert(current.right, value)

    def parallel_search(self, target):
        with ProcessPoolExecutor() as executor:
            future = executor.submit(self._search, self.root, target)
            return future.result()

    def _search(self, node, target):
        if node is None:
            return False
        if node.value == target:
            return True
        return self._search(node.left, target) or self._search(node.right, target)

def measure_search_time(tree, target):
    start = time.time()
    found = tree.parallel_search(target)
    end = time.time()
    return end - start, found


def teste_com_diferentes_tamanhos_arvore():
    tamanhos_arvor_sem_duplic = [2**i for i in range(10)]
    times = []

    for size in tamanhos_arvor_sem_duplic:
        bt = BinaryTree()
        values = random.sample(range(size * 10), size)
        for v in values:
            bt.insert(v)

        target = random.choice(values)

        exec_time, found = measure_search_time(bt, target)
        times.append(exec_time)

        print(f"Árvore com {size} nós - Tempo: {exec_time:.6f}s - Encontrado: {found}")



    plt.plot(tamanhos_arvor_sem_duplic, times, marker="o", linestyle="-")
    plt.xlabel("Tamanho da Árvore (nós)")
    plt.ylabel("Tempo de Busca (milissegundos)")
    plt.title("Tempo de Busca Paralela em Árvore Binária")
    plt.grid()
    plt.show()

def exercicio52():
    teste_com_diferentes_tamanhos_arvore()

if __name__ == '__main__':
    exercicio52()
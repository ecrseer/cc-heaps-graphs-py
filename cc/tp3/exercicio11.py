import time
import matplotlib.pyplot as plt

class Node:
    def __init__(self, valor):
        self.valor = valor
        self.left = None
        self.right = None


class ArvoreBinaria:
    def __init__(self):
        self.root = None

    def add(self, valor):
        if self.root is None:
            self.root = Node(valor)
        else:
            self._add_no_node(valor, self.root)

    def _add_no_node(self, valor, node):
        if valor < node.valor:
            if node.left is None:
                node.left = Node(valor)
            else:
                self._add_no_node(valor, node.left)
        else:
            if node.right is None:
                node.right = Node(valor)
            else:
                self._add_no_node(valor, node.right)

    def inorder(self):
        return self._traverse_inorder(self.root, [])

    def _traverse_inorder(self, node, result):
        if node:
            self._traverse_inorder(node.left, result)
            result.append(node.valor)
            self._traverse_inorder(node.right, result)
        return result

    def preorder(self):
        return self._traverse_preorder(self.root, [])

    def _traverse_preorder(self, node, result):
        if node:
            result.append(node.valor)
            self._traverse_preorder(node.left, result)
            self._traverse_preorder(node.right, result)
        return result

    def postorder(self):
        return self._traverse_postorder(self.root, [])

    def _traverse_postorder(self, node, result):
        if node:
            self._traverse_postorder(node.left, result)
            self._traverse_postorder(node.right, result)
            result.append(node.valor)
        return result


def exercicio11():
    arvore = ArvoreBinaria()
    notas=[50, 30, 70, 20, 40, 60, 80, 5, 11, 12, 72, 1, 63, 94, 72, 74, 77, 95, 40, 39, 32, 25, 65, 5, 53, 61, 65, 59, 50, 6, 78, 96, 3, 0, 82, 24, 93, 93, 99, 44, 78, 11, 37, 43, 66, 32, 85, 100, 46, 77, 99, 29, 72, 69, 71, 46, 82]

    for nota in notas:
        arvore.add(nota)

    print("\n---- exercicio 11 ----")
    print("\nValores:", notas)

    tempos = []
    percursos = ["In-order", "Pre-order", "Post-order"]

    inicio = time.time()
    inorder = arvore.inorder()
    tempos.append(time.time() - inicio)
    print(f"In-order ({tempos[-1]:.6f}s):", inorder)

    inicio = time.time()
    preorder = arvore.preorder()
    tempos.append(time.time() - inicio)
    print(f"Pre-order ({tempos[-1]:.6f}s):", preorder)

    inicio = time.time()
    postorder = arvore.postorder()
    tempos.append(time.time() - inicio)
    print(f"Post-order ({tempos[-1]:.6f}s):", postorder)

    plot_this(percursos, tempos)


def plot_this(percursos, tempos):
    plt.figure(figsize=(8, 5))
    plt.plot(percursos, [t * 1000 for t in tempos], marker='o', linestyle='-', color='b')
    plt.xlabel("Tipo de Percurso")
    plt.ylabel("Tempo total (ms)")
    plt.title("Tempos de Execução dos Percursos na Árvore Binária")
    plt.grid()
    plt.show()

exercicio11()
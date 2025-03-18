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

    def remover(self, valor):
        self.root = self._remover_no(self.root, valor)

    def _remover_no(self, node, valor):
        if node is None:
            return node

        if valor < node.valor:
            node.left = self._remover_no(node.left, valor)
        elif valor > node.valor:
            node.right = self._remover_no(node.right, valor)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            sucessor = self._min_value_node(node.right)
            node.valor = sucessor.valor
            node.right = self._remover_no(node.right, sucessor.valor)

        return node

    def _min_value_node(self, node):
        atual = node
        while atual.left is not None:
            atual = atual.left
        return atual

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


def exercicio_12():
    arvore = ArvoreBinaria()
    notas = [50, 30, 70, 20, 40, 60, 80]
    for nota in notas:
        arvore.add(nota)

    print("\n---- Remoção de Nós ----")

    tempos_remocao = []


    nos_para_remover = [20, 30, 50]

    for valor in nos_para_remover:
        inicio = time.time()
        arvore.remover(valor)
        fim = time.time() - inicio
        tempos_remocao.append(fim)
        print(f"Removido {valor} ({fim:.12f}s)")

    plot_this(nos_para_remover, tempos_remocao)


def plot_this(nos_removidos, tempos):
    plt.figure(figsize=(8, 5))
    plt.plot(nos_removidos, tempos, marker='o', linestyle='-')
    plt.xlabel("Nó Removido")
    plt.ylabel("Tempo de Remoção (ms)")
    plt.title("Tempos de Remoção na BST")
    plt.grid()
    plt.show()


exercicio_12()

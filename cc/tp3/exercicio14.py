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
        inicio = time.time()
        result = self._traverse_inorder(self.root, [])
        duracao = time.time() - inicio
        return result, duracao

    def _traverse_inorder(self, node, result):
        if node:
            self._traverse_inorder(node.left, result)
            result.append(node.valor)
            self._traverse_inorder(node.right, result)
        return result

    def preorder(self):
        inicio = time.time()
        result = self._traverse_preorder(self.root, [])
        duracao = time.time() - inicio
        return result, duracao

    def _traverse_preorder(self, node, result):
        if node:
            result.append(node.valor)
            self._traverse_preorder(node.left, result)
            self._traverse_preorder(node.right, result)
        return result

    def postorder(self):
        inicio = time.time()
        result = self._traverse_postorder(self.root, [])
        duracao = time.time() - inicio
        return result, duracao

    def _traverse_postorder(self, node, result):
        if node:
            self._traverse_postorder(node.left, result)
            self._traverse_postorder(node.right, result)
            result.append(node.valor)
        return result

    def is_bst(self):
        inicio = time.time()
        result = self._is_bst_util(self.root, float('-inf'), float('inf'))
        duracao = time.time() - inicio
        return result, duracao

    def _is_bst_util(self, node, min_val, max_val):
        if node is None:
            return True

        if not (min_val < node.valor < max_val):
            return False

        return (self._is_bst_util(node.left, min_val, node.valor) and
                self._is_bst_util(node.right, node.valor, max_val))


def cria_arvore_verifica(notas=[50, 30, 70, 20, 40, 60, 80]):
    arvore = ArvoreBinaria()
    for nota in notas:
        arvore.add(nota)

    print("\nValores:", notas)


    is_bst, duracao_bst = arvore.is_bst()
    return duracao_bst

def exercicio14():
    temp1=cria_arvore_verifica()
    print(f"duracao arvore com 7  ({temp1:.12f}s")

    av2 = [421,42,55,1]
    temp2=cria_arvore_verifica(av2)
    print(f"duracao arvore com {len(av2)} ({temp2:.12f}s")

    av3 = [5123,3,4,18,55,2,4,2,1,5,8,5,3]
    temp3=cria_arvore_verifica(av3)
    print(f"duracao arvore com {len(av3)} ({temp3:.12f}s")

    plot_this(["Árvore 1", "Árvore 2", "Árvore 3"], [temp1,temp2,temp3])


def plot_this(valores_para_buscar, busca_tempos):
    plt.figure(figsize=(10, 6))
    plt.plot(valores_para_buscar, [t * 1000 for t in busca_tempos], marker='o', linestyle='-', color='orange')
    plt.xlabel("Valor Buscado")
    plt.ylabel("Tempo de Busca (ms)")
    plt.title("Tempos Individuais de Busca")
    plt.grid()
    plt.tight_layout()
    plt.show()

exercicio14()
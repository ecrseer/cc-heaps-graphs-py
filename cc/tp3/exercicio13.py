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

    def buscar(self, valor):
        if self.root is None:
            return False
        return self._buscar_no_node(self.root, valor)

    def _buscar_no_node(self, node_atual, valor):
        if node_atual is None:
            return False
        if valor == node_atual.valor:
            return True
        if valor < node_atual.valor:
            return self._buscar_no_node(node_atual.left, valor)
        return self._buscar_no_node(node_atual.right, valor)


def exercicio13():
    arvore = ArvoreBinaria()
    notas = [50, 30, 70, 20, 40, 60, 80]
    for nota in notas:
        arvore.add(nota)

    print("\n---- Exercício 13 ----")
    print("\nValores:", notas)


    valores_para_buscar = [20, 40, 60, 80, 90]
    busca_tempos = []
    for valor in valores_para_buscar:
        inicio = time.time()
        encontrado = arvore.buscar(valor)
        tempo_busca = time.time() - inicio
        busca_tempos.append(tempo_busca)
        print(f"Buscar {valor} ({tempo_busca:.12f}s): {'Encontrado' if encontrado else 'Não Encontrado'}")

    plot_this(valores_para_buscar, busca_tempos)


def plot_this(valores_para_buscar, busca_tempos):
    plt.figure(figsize=(10, 6))
    plt.plot(valores_para_buscar, [t * 1000 for t in busca_tempos], marker='o', linestyle='-', color='orange')
    plt.xlabel("Valor Buscado")
    plt.ylabel("Tempo de Busca (ms)")
    plt.title("Tempos Individuais de Busca")
    plt.grid()
    plt.tight_layout()
    plt.show()


exercicio13()
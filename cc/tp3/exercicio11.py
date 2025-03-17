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

    def buscar(self, valor):
        if self.root is None:
            return False
        else:
            return self._buscar_no_node(self.root, valor)

    def _buscar_no_node(self, node_atual, valor):
        if node_atual is None:
            return False
        if valor == node_atual.valor:
            return True
        if valor < node_atual.valor:
            return self._buscar_no_node(node_atual.left, valor)
        return self._buscar_no_node(node_atual.right, valor)

    def busca_min(self):
        if self.root is None:
            return None
        atual = self.root
        while atual.left is not None:
            atual = atual.left
        return atual.valor

    def busca_max(self):
        if self.root is None:
            return None
        atual = self.root
        while atual.right is not None:
            atual = atual.right
        return atual.valor

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
    notas = [50, 30, 70, 20, 40, 60, 80]
    for nota in notas:
        arvore.add(nota)

    print("In-order:", arvore.inorder())
    print("Pre-order:", arvore.preorder())
    print("Post-order:", arvore.postorder())


exercicio11()

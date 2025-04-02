class Grafo:
    def __init__(self):
        self.lista_adjacencia = {}

    def adicionar_vertice(self, vertice):
        if vertice not in self.lista_adjacencia:
            self.lista_adjacencia[vertice] = []

    def adicionar_aresta(self, vertice1, vertice2):
        if vertice1 in self.lista_adjacencia and vertice2 in self.lista_adjacencia:
            self.lista_adjacencia[vertice1].append(vertice2)
            self.lista_adjacencia[vertice2].append(vertice1)

    def mostrar_grafo(self):
        print("\nLista de Adjacência:\n")
        for vertice in self.lista_adjacencia:
            print(f"{vertice} -> {self.lista_adjacencia[vertice]}")

    def mostrar_vizinhos(self, vertice):
        if vertice in self.lista_adjacencia:
            print(f"Vizinhos de {vertice}: {self.lista_adjacencia[vertice]}")
        else:
            print(f"O vértice {vertice} não existe no grafo.")

    def dfs_recursivo(self, vert_atual, visitados=None):
        # Executa a busca em profundidade (DFS) de forma recursiva para explorar rotas.
        if visitados is None:
            visitados = set()

        print(vert_atual, end=" => ")
        visitados.add(vert_atual)  # Marca como visitado

        for vizinho in self.lista_adjacencia[vert_atual]:
            if vizinho not in visitados:
                self.dfs_recursivo(vizinho, visitados)

        return visitados


estacoes = ["A", "B", "C", "D", "E", "F"]
grafo = Grafo()
for estacao in estacoes:
    grafo.adicionar_vertice(estacao)

# Adicionando conexões entre estações
conexoes = [("A", "B"), ("A", "C"), ("B", "A"), ("B", "D"), ("B", "E"),
            ("C", "A"), ("C", "F"), ("D", "B"), ("D", "E"), ("E", "B"),
            ("E", "D"), ("E", "F"), ("F", "C"), ("F", "E")]
for est1, est2 in conexoes:
    grafo.adicionar_aresta(est1, est2)


print("DFS  a partir de A:")
grafo.dfs_recursivo("A")

grafo.mostrar_grafo()

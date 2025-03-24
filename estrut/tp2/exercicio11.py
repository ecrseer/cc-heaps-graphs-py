class Grafo:
    def __init__(self):
        self.lista_adjacencia = {}

    def adicionar_vertice(self, vertice):
        # Adiciona um vértice ao grafo.
        if vertice not in self.lista_adjacencia:
            self.lista_adjacencia[vertice] = []

    def adicionar_aresta(self, vertice1, vertice2):
        # Adiciona uma aresta não-direcionada entre dois vértices.
        self.lista_adjacencia[vertice1].append(vertice2)
        self.lista_adjacencia[vertice2].append(vertice1)

    def dfs_recursivo(self, vertice, visitados=None):
        # Executa a busca em profundidade de forma recursiva.
        if visitados is None:
            visitados = set()

        print(vertice, end=" ")
        visitados.add(vertice)

        for vizinho in self.lista_adjacencia[vertice]:
            if vizinho not in visitados:
                self.dfs_recursivo(vizinho, visitados)


grafo = Grafo()
vertices = ["A", "B", "C", "D", "E"]
for v in vertices:
    grafo.adicionar_vertice(v)

arestas = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "E")]

for v1, v2 in arestas:
    grafo.adicionar_aresta(v1, v2)

print("Busca em Profundidade (DFS) iniciando em A:")
grafo.dfs_recursivo("A")

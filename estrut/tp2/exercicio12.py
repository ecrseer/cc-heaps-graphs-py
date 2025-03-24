class Grafo:
    def __init__(self):
        # Inicializa um grafo como um dicionário de listas de adjacência."
        self.lista_adjacencia = {}

    def adicionar_vertice(self, vertice):
        if vertice not in self.lista_adjacencia:
            self.lista_adjacencia[vertice] = []

    def adicionar_aresta(self, vertice1, vertice2):
        if vertice1 in self.lista_adjacencia and vertice2 in self.lista_adjacencia:
            self.lista_adjacencia[vertice1].append(vertice2)
            self.lista_adjacencia[vertice2].append(vertice1)

    def bfs(self, inicio):
        # Realiza a Busca em Largura (BFS) a partir do vértice de início.
        visitados = set()
        fila = [inicio]

        while fila:
            vertice = fila.pop(0)
            if vertice not in visitados:
                print(vertice, end=" ")
                visitados.add(vertice)
                fila.extend(self.lista_adjacencia[vertice])

    def mostrar_grafo(self):
        """Exibe o grafo na forma de lista de adjacência"""
        for vertice in self.lista_adjacencia:
            print(f"{vertice} -> {self.lista_adjacencia[vertice]}")


grafo = Grafo()
vertices = ["A", "B", "C", "D", "E", "F"]
for v in vertices:
    grafo.adicionar_vertice(v)

arestas = [("A", "B"), ("A", "C"), ("B", "D"), ("B", "E"), ("C", "F")]
for v1, v2 in arestas:
    grafo.adicionar_aresta(v1, v2)

print("""exercicio 12
--------------------------------""")
print("Lista de Adjacência do Grafo:")
grafo.mostrar_grafo()

print("\n\nBusca em Largura (BFS) a partir de A:")
grafo.bfs("A")

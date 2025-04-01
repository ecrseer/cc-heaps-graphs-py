class MatrizGrafo:
    def __init__(self, bairros):
        self.vertice = bairros
        self.V = len(bairros)
        self.grafo = [[0] * self.V for _ in range(self.V)]

    def adicionar_aresta(self, origem, destino, peso):
        u, v = self.obtem_indice_por_nome(origem, destino)
        self.grafo[u][v] = peso
        self.grafo[v][u] = peso  # Grafo não direcionado

    def obtem_indice_por_nome(self, origem, destino):
        u = self.vertice.index(origem)
        v = self.vertice.index(destino)
        return u, v

    def exibir_grafo(self):
        print("\nMatriz de Adjacência:")
        print("   " + "  ".join(self.vertice))  # Header row
        for i, linha in enumerate(self.grafo):
            print(f"{self.vertice[i]} {linha}")  # Row header + matrix row


print("""------------------------------------------
------------------------------------------""")




class ListaAdjacente:
    def __init__(self):
        self.lista_adjacencia = {}

    def adicionar_vertice(self, vertice):
        """Adiciona um novo vértice ao grafo"""
        if vertice not in self.lista_adjacencia:
            self.lista_adjacencia[vertice] = []

    def adicionar_aresta(self, vertice1, vertice2, peso):
        """Adiciona uma aresta entre dois vértices com peso"""
        if vertice1 in self.lista_adjacencia and vertice2 in self.lista_adjacencia:
            self.lista_adjacencia[vertice1].append((vertice2, peso))
            self.lista_adjacencia[vertice2].append((vertice1, peso))  # Grafo não direcionado

    def mostrar_grafo(self):
        """Exibe o grafo na forma de lista de adjacência"""
        print("\nLista de Adjacência:")
        for vertice, vizinhos in self.lista_adjacencia.items():
            vizinhos_str = ", ".join(f"{v}({p})" for v, p in vizinhos)
            print(f"{vertice} -> {vizinhos_str}")

    def mostrar_vizinhos(self, vertice):
        """Exibe os vizinhos de um determinado vértice"""
        if vertice in self.lista_adjacencia:
            print(f"Vizinhos de {vertice}: {self.lista_adjacencia[vertice]}")
        else:
            print(f"O vértice {vertice} não existe no grafo.")




vertices = ["A", "B", "C", "D", "E", "F"]


g_matriz = MatrizGrafo(vertices)
g_lista = ListaAdjacente()


arestas = [
    ("A", "B", 4), ("A", "C", 2),
    ("B", "D", 5),
    ("C", "D", 8), ("C", "E", 3),
    ("D", "F", 6),
    ("E", "F", 1)
]

for vertice in vertices:
    g_lista.adicionar_vertice(vertice)

for origem, destino, peso in arestas:
    g_matriz.adicionar_aresta(origem, destino, peso)
    g_lista.adicionar_aresta(origem, destino, peso)

g_matriz.exibir_grafo()
print("------------------------------------------")
g_lista.mostrar_grafo()




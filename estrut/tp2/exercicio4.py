class Grafo:
    def __init__(self):
        self.lista_adjacencia = {}  # Dicionário para armazenar o grafo

    def adicionar_vertice(self, vertice):
        """Adiciona um novo vértice ao grafo"""
        if vertice not in self.lista_adjacencia:
            self.lista_adjacencia[vertice] = []

            # A, B, C

            # "A"; []
            # "B"; []
            # "C"; []

    def adicionar_aresta(self, vertice1, vertice2):
        """Adiciona uma aresta entre dois vértices"""
        if vertice1 in self.lista_adjacencia and vertice2 in self.lista_adjacencia:
            self.lista_adjacencia[vertice1].append(vertice2)
            self.lista_adjacencia[vertice2].append(vertice1)

    def mostrar_grafo(self):
        """Exibe o grafo na forma de lista de adjacência"""
        for vertice in self.lista_adjacencia:
            print(f"{vertice} -> {self.lista_adjacencia[vertice]}")

    def mostrar_vizinhos(self, vertice):
        """Exibe os vizinhos de um determinado vértice"""
        if vertice in self.lista_adjacencia:
            print(f"Vizinhos de {vertice}: {self.lista_adjacencia[vertice]}")
        else:
            print(f"O vértice {vertice} não existe no grafo.")


grafo = Grafo()

for v in ["Centro", "Bairro A", "Bairro B", "Bairro C", "Bairro D"]:
    grafo.adicionar_vertice(v)
    

arestas = [("Centro", "Bairro A"), ("Centro", "Bairro B"),
           ("Bairro A", "Bairro C"), ("Bairro B", "Bairro C"),
           ("Bairro C", "Bairro D")]

for v1, v2 in arestas:
    grafo.adicionar_aresta(v1, v2)

print("Lista de Adjacência do Grafo:")
grafo.mostrar_grafo()

grafo.mostrar_vizinhos("Centro")

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

    def mostrar_grafo(self):
        """Exibe o grafo na forma de lista de adjacência"""
        print("""
        Lista de Adjacência:
        """)
        for vertice in self.lista_adjacencia:
            print(f"{vertice} -> {self.lista_adjacencia[vertice]}")

    def mostrar_vizinhos(self, vertice):
        """Exibe os vizinhos de um determinado vértice"""
        if vertice in self.lista_adjacencia:
            print(f"Vizinhos de {vertice}: {self.lista_adjacencia[vertice]}")
        else:
            print(f"O vértice {vertice} não existe no grafo.")

    def bfs(self, inicio):
        # Realiza a Busca em Largura (BFS) a partir do vértice de início.
        visitados = set()  # Conjunto para armazenar vértices visitados
        fila = [inicio]  # Lista usada como fila (FIFO)

        while fila:
            vertice = fila.pop(0)  # Remove o primeiro elemento da fila
            if vertice not in visitados:
                print(vertice, end=" ")  # Exibe o nó visitado
                visitados.add(vertice)  # Marca como visitado
                fila.extend(self.lista_adjacencia[vertice])  # Adiciona vizinhos à fila


# Criando o grafo
grafo = Grafo()
vertices = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
for v in vertices:
    grafo.adicionar_vertice(v)

# Adicionando arestas
arestas = [("A", "B"), ("A", "C"), ("B", "D"), ("B", "E"), ("C", "F"), ("F", "G"), ("F", "H"), ("H", "I"), ("H", "J")]
for v1, v2 in arestas:
    grafo.adicionar_aresta(v1, v2)

# Executando BFS a partir do nó "A"
print("Busca em Largura (BFS) a partir de A:")
grafo.bfs("A")
grafo.mostrar_grafo()

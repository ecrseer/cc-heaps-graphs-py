class GrafoMatriz:
    def __init__(self, num_vertices,direcao='nao_direcionado'):
        self.num_vertices = num_vertices
        self.matriz = [[0] * num_vertices for _ in range(num_vertices)]
        self.vertices = {}  # Mapeia nomes para índices
        self.indice_para_vertice = {}  # Mapeia índices para nomes
        self.contador = 0  # Controla a adição de vértices
        self.direcao = direcao

    def adicionar_vertice(self, vertice):
        """Adiciona um novo vértice ao grafo"""
        if vertice not in self.vertices and self.contador < self.num_vertices:
            self.vertices[vertice] = self.contador
            self.indice_para_vertice[self.contador] = vertice
            self.contador += 1

    def adicionar_aresta(self, vertice1, vertice2):
        """Adiciona uma aresta entre dois vértices"""
        if vertice1 in self.vertices and vertice2 in self.vertices:
            i, j = self.vertices[vertice1], self.vertices[vertice2]
            self.matriz[i][j] = 1
            if(self.direcao == 'nao_direcionado'):
                self.matriz[j][i] = 1

    def mostrar_matriz(self):
        """Exibe a matriz de adjacência"""
        print("Matriz de Adjacência:")
        print("  ", "  ".join(self.vertices.keys()))  # Cabeçalho
        for i, linha in enumerate(self.matriz):
            print(self.indice_para_vertice[i], linha)


print("""----------
Exercicio 3

""")

def mostra_nao_direcionado():
    grafo = GrafoMatriz(4)
    for v in ["A", "B", "C", "D"]:
        grafo.adicionar_vertice(v)
    arestas = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D")]
    for v1, v2 in arestas:
        grafo.adicionar_aresta(v1, v2)

    print("Grafo não direcionado:")
    grafo.mostrar_matriz()
    print()


mostra_nao_direcionado()




def mostra_direcionado():
    grafo = GrafoMatriz(4,'direcionado')
    for v in ["A", "B", "C", "D"]:
        grafo.adicionar_vertice(v)
    arestas = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D")]
    for v1, v2 in arestas:
        grafo.adicionar_aresta(v1, v2)


    print("\nGrafo direcionado:")
    grafo.mostrar_matriz()


mostra_direcionado()

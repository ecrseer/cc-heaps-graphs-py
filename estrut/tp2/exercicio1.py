class GrafoMatriz:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.matriz = [[0] * num_vertices for _ in range(num_vertices)]
        self.vertices = {}  # Mapeia nomes para índices
        self.indice_para_vertice = {}  # Mapeia índices para nomes
        self.contador = 0  # Controla a adição de vértices

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
            self.matriz[j][i] = 1


    def mostrar_matriz(self):
        """Exibe a matriz de adjacência"""
        print("Matriz de Adjacência:")
        print("  ", "  ".join(self.vertices.keys()))  # Cabeçalho
        for i, linha in enumerate(self.matriz):
            print(self.indice_para_vertice[i], linha)

    def mostrar_vizinhos(self, vertice):
        """Exibe os vizinhos de um determinado vértice"""
        if vertice in self.vertices:
            indice = self.vertices[vertice]
            vizinhos = [self.indice_para_vertice[i] for i in range(self.num_vertices) if self.matriz[indice][i] == 1]
            print(f"Vizinhos de {vertice}: {vizinhos}")
        else:
            print(f"O vértice {vertice} não existe no grafo.")


# Criando o grafo com bairros do Rio de Janeiro
grafo = GrafoMatriz(6)

# Adicionando bairros (vértices)
bairros = ["Copacabana", "Ipanema", "Botafogo", "Flamengo", "Leme", "Leblon"]
for bairro in bairros:
    grafo.adicionar_vertice(bairro)

# Adicionando ruas (arestas)
ruas = [("Copacabana", "Leme"), ("Copacabana", "Botafogo"), ("Copacabana", "Ipanema"),
        ("Ipanema", "Leblon"), ("Botafogo", "Flamengo"), ("Ipanema", "Flamengo")]

for bairro1, bairro2 in ruas:
    grafo.adicionar_aresta(bairro1, bairro2)

# Exibindo a matriz de adjacência
grafo.mostrar_matriz()

# Exibindo vizinhos de um bairro específico
grafo.mostrar_vizinhos("Copacabana")
grafo.mostrar_vizinhos("Ipanema")


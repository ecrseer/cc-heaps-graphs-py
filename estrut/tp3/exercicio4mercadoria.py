class ListaAdjacente:
    def __init__(self):
        self.lista_adjacencia = {}

    def adicionar_vertice(self, vertice):
        """Adiciona um novo vértice ao grafo"""
        if vertice not in self.lista_adjacencia:
            self.lista_adjacencia[vertice] = []

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


class GrafoPonderado:
    def __init__(self):
        self.vertices = {}
        self.listaAdj = ListaAdjacente()

    def adicionar_vertic(self, cidade):
        if cidade not in self.vertices:
            self.vertices[cidade] = {}
            self.listaAdj.adicionar_vertice(cidade)

    def adicionar_rua(self, cidade1, cidade2, tempo):
        self.vertices[cidade1][cidade2] = tempo
        self.vertices[cidade2][cidade1] = tempo
        self.listaAdj.adicionar_aresta(cidade1, cidade2)

    def dijkstra(self, origem, destino):
        nao_visitados = list(self.vertices.keys())
        distancias = {cidade: float("inf") for cidade in self.vertices}
        distancias[origem] = 0
        predecessores = {}

        while nao_visitados:
            bairro_atual = min(nao_visitados, key=lambda bairro: distancias[bairro])

            if distancias[bairro_atual] == float("inf"):
                break

            for vizinho, distancia in self.vertices[bairro_atual].items():
                nova_distancia = distancias[bairro_atual] + distancia
                if nova_distancia < distancias[vizinho]:
                    distancias[vizinho] = nova_distancia
                    predecessores[vizinho] = bairro_atual

            nao_visitados.remove(bairro_atual)

        caminho = []
        bairro_atual = destino
        while bairro_atual in predecessores:
            caminho.append(bairro_atual)
            bairro_atual = predecessores[bairro_atual]
        caminho.append(origem)
        caminho.reverse()

        return caminho, distancias[destino]

print("""------------------------------------------
exercicio 4 - Transporte de mercadorias - Djkstra:
------------------------------------------""")

logistica = GrafoPonderado()

cidades = ["SP", "RJ", "BSB", "BH", "FLN", "POA"]

for cidade in cidades:
    logistica.adicionar_vertic(cidade)

rotas = [
    ("SP", "RJ", 4), ("SP", "BSB", 3), ("SP", "POA", 5),
    ("RJ", "BH", 2), ("RJ", "POA", 6),
    ("BSB", "FLN", 7), ("BSB", "POA", 4),
    ("BH", "FLN", 6), ("BH", "POA", 3),
    ("POA", "FLN", 5)
]

for cidade1, cidade2, distancia in rotas:
    logistica.adicionar_rua(cidade1, cidade2, distancia)

print("""
Cidades e adjacências:""")
logistica.listaAdj.mostrar_grafo()

origem = "RJ"
destino = "FLN"
print(f"\nEncontrando a rota mais curta entre {origem} e {destino}: ")
rota, distancia = logistica.dijkstra(origem, destino)

print(f"\nMelhor rota de {origem} para {destino}:\n {' => '.join(rota)}")
print(f"Distância total: {distancia} km")

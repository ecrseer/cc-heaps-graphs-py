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
exercicio 3 - Rede transportes - Aeroporto@:
------------------------------------------""")

logistica = GrafoPonderado()

aeroportos = ["GRU", "GIG", "BSB", "CNF", "SDU", "POA"]

for aeroporto in aeroportos:
    logistica.adicionar_vertic(aeroporto)

rotas = [
    ("GRU", "GIG", 4), ("GRU", "BSB", 3), ("GRU", "POA", 5),
    ("GIG", "CNF", 2), ("GIG", "POA", 6),
    ("BSB", "SDU", 7), ("BSB", "POA", 4),
    ("CNF", "SDU", 6), ("CNF", "POA", 3),
    ("POA", "SDU", 5)
]

for centro1, centro2, distancia in rotas:
    logistica.adicionar_rua(centro1, centro2, distancia)

print("""
Bairros e adjacencias:""")
logistica.listaAdj.mostrar_grafo()

origem = "GIG"
destino = "SDU"
print(f"\nEncontrando a rota  de onibus mais curta entre o bairro {origem} e centro {destino}: ")
rota, distancia = logistica.dijkstra(origem, destino)

print(f"\nMelhor rota de {origem} para {destino}:\n {' => '.join(rota)}")
print(f"Distância total: {distancia} km")

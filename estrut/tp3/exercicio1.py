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

    def adicionar_estrada(self, cidade1, cidade2, tempo):
        self.vertices[cidade1][cidade2] = tempo
        self.vertices[cidade2][cidade1] = tempo
        self.listaAdj.adicionar_aresta(cidade1, cidade2)

    def dijkstra(self, origem, destino):
        nao_visitados = list(self.vertices.keys())
        distancias = {cidade: float("inf") for cidade in self.vertices}
        distancias[origem] = 0
        predecessores = {}

        while nao_visitados:
            cidade_atual = min(nao_visitados, key=lambda cidade: distancias[cidade])

            if distancias[cidade_atual] == float("inf"):
                break

            for vizinho, distancia in self.vertices[cidade_atual].items():
                nova_distancia = distancias[cidade_atual] + distancia
                if nova_distancia < distancias[vizinho]:
                    distancias[vizinho] = nova_distancia
                    predecessores[vizinho] = cidade_atual

            nao_visitados.remove(cidade_atual)

        caminho = []
        cidade_atual = destino
        while cidade_atual in predecessores:
            caminho.append(cidade_atual)
            cidade_atual = predecessores[cidade_atual]
        caminho.append(origem)
        caminho.reverse()

        return caminho, distancias[destino]


print("""------------------------------------------
exercicio 1 - logistica entregas:
------------------------------------------""")

logistica = GrafoPonderado()
centros_distri = ["Cop", "Bot", "Cax", "Dac", "Fla", "Gav"]

for centro in centros_distri:
    logistica.adicionar_vertic(centro)

conexoes = [
    ("Cop", "Bot", 4), ("Cop", "Cax", 3), ("Cop", "Gav", 5),
    ("Bot", "Dac", 2), ("Bot", "Gav", 6),
    ("Cax", "Fla", 7), ("Cax", "Gav", 4),
    ("Dac", "Fla", 6), ("Dac", "Gav", 3),
    ("Gav", "Fla", 5)
]

for centro1, centro2, distancia in conexoes:
    logistica.adicionar_estrada(centro1, centro2, distancia)

print("""
Demonstrando lista de adjacencia dos centros:""")
logistica.listaAdj.mostrar_grafo()

print("""
demonstrando vizinhos do centro Bot:""")
logistica.listaAdj.mostrar_vizinhos("Bot")

origem = "Cax"
destino = "Bot"
print(f"\nEncontrando a rota mais curta entre o centro {origem} e centro {destino}: ")
rota, distancia = logistica.dijkstra(origem, destino)

print(f"\nMelhor rota de {origem} para {destino}: {' => '.join(rota)}")
print(f"Distância total: {distancia} km")

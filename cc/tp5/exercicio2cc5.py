class GrafPondDijkstra:
    def __init__(self):
        self.vertices = {}

    def dijkstra(self, origem):
        nao_visitados = list(self.vertices.keys())
        distancias = {cidade: float("inf") for cidade in self.vertices}
        distancias[origem] = 0
        predecessores = {}

        while nao_visitados:
            bairro_atual = min(nao_visitados, key=lambda bairro: distancias[bairro])

            if distancias[bairro_atual] == float("inf"):
                break

            for vizinho, distancia in self.vertices[bairro_atual]:
                nova_distancia = distancias[bairro_atual] + distancia
                if nova_distancia < distancias[vizinho]:
                    distancias[vizinho] = nova_distancia
                    predecessores[vizinho] = bairro_atual

            nao_visitados.remove(bairro_atual)

        return distancias, predecessores

    def menor_caminho(self, origem, destino, predecessores):
        caminho = []
        bairro_atual = destino
        while bairro_atual in predecessores:
            caminho.append(bairro_atual)
            bairro_atual = predecessores[bairro_atual]
        caminho.append(origem)
        caminho.reverse()
        return caminho


print("""------------------------------------------
exercicio 1.1 - Dijkstra (Caminhos Mínimos):
------------------------------------------""")

vertices_adjacen = {
    "A": [("B", 1), ("C", 4)],
    "B": [("A", 1), ("C", 2), ("D", 5)],
    "C": [("A", 4), ("B", 2), ("D", 1)],
    "D": [("B", 5), ("C", 1)]
}

print(f"Vertices Adjacentes: ")
for vertice, vizinhos in vertices_adjacen.items():
    print(f"{vertice}: {vizinhos}")

grafoLgst = GrafPondDijkstra()
grafoLgst.vertices = vertices_adjacen

origem = "A"
destino = "D"
distancias, predecessores = grafoLgst.dijkstra(origem)
caminho = grafoLgst.menor_caminho(origem, destino, predecessores)

print("\nvertices adjacentes:")
for vertice, distancia in distancias.items():
    print(f"Distância até {vertice}: {distancia}")

print(f"\nMelhor rota de {origem} para {destino}: {' => '.join(caminho)}")

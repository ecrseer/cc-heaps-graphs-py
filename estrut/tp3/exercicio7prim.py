class PrimGrafoFibraOtica:
    def __init__(self, bairros):
        self.bairros = bairros
        self.V = len(bairros)
        self.grafo = [[0] * self.V for _ in range(self.V)]

    def adicionar_aresta(self, origem, destino, peso):

        u, v = self.obtem_indice_por_nome(origem, destino)
        self.grafo[u][v] = peso
        self.grafo[v][u] = peso

    def obtem_indice_por_nome(self, origem, destino):
        u = self.bairros.index(origem)
        v = self.bairros.index(destino)
        return u, v

    def prim(self):
        infinito = float('inf')
        selecionado = [False] * self.V
        chave = [infinito] * self.V
        pai = [-1] * self.V
        chave[0] = 0

        for _ in range(self.V):
            minimo = infinito
            vertice_selecionado = -1
            for v in range(self.V):
                if not selecionado[v] and chave[v] < minimo:
                    minimo = chave[v]
                    vertice_selecionado = v

            selecionado[vertice_selecionado] = True

            for v in range(self.V):
                if 0 < self.grafo[vertice_selecionado][v] < chave[v] and not selecionado[v]:
                    chave[v] = self.grafo[vertice_selecionado][v]
                    pai[v] = vertice_selecionado

        print("\nArestas da Árvore Geradora Mínima:")
        custo_total = 0
        for i in range(1, self.V):
            origem = self.bairros[pai[i]]
            destino = self.bairros[i]
            print(f"{origem} - {destino} (Peso: {self.grafo[i][pai[i]]})")
            custo_total += self.grafo[i][pai[i]]
        print(f"Peso total da AGM: {custo_total}")


print("""------------------------------------------
Exercício 7 - Fibra ótica entre bairros:
------------------------------------------""")

bairros = ["Copacabana", "Ipanema", "Leblon", "Botafogo", "Tijuca", "Centro"]

g = PrimGrafoFibraOtica(bairros)

arestas = [
    ("Copacabana", "Ipanema", 4), ("Copacabana", "Leblon", 2), ("Ipanema", "Leblon", 5),
    ("Ipanema", "Botafogo", 10), ("Leblon", "Botafogo", 8), ("Leblon", "Tijuca", 3),
    ("Botafogo", "Tijuca", 7), ("Botafogo", "Centro", 6), ("Tijuca", "Centro", 1)
]

for origem, destino, peso in arestas:
    g.adicionar_aresta(origem, destino, peso)

g.prim()

class PrimGrafo:
    def __init__(self, cidades):
        self.cidades = cidades
        self.V = len(cidades)
        self.grafo = [[0] * self.V for _ in range(self.V)]

    def adicionar_aresta(self, origem, destino, peso):
        u, v = self.obtem_indice_por_nome(origem, destino)
        self.grafo[u][v] = peso
        self.grafo[v][u] = peso

    def obtem_indice_por_nome(self, origem, destino):
        u = self.cidades.index(origem)
        v = self.cidades.index(destino)
        return u, v

    def exibir_grafo_matriz(self):
        print("\nMatriz de Adjacência:")
        cabecalho= [cidade[0] for cidade in self.cidades]
        print("      " + "  ".join(cabecalho))
        for i, linha in enumerate(self.grafo):
            print(f"{self.cidades[i]} {linha}")

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
            origem = self.cidades[pai[i]]
            destino = self.cidades[i]
            print(f"{origem} - {destino} (Custo instalacao: {self.grafo[i][pai[i]]})")
            custo_total += self.grafo[i][pai[i]]
        print(f"Peso total da AGM: {custo_total}")


print("""------------------------------------------
Exercício 10 - Algoritmo Guloso - internet para cidades 
------------------------------------------""")
cidades = ["Nite", "Reci", "Salv", "Jund", "Cuiá"]

g = PrimGrafo(cidades)

arestas = [
    ("Nite", "Reci", 2),
    ("Reci", "Salv", 8),
    ("Reci", "Jund", 3),
    ("Salv", "Jund", 7),
    ("Salv", "Cuiá", 6),
    ("Jund", "Cuiá", 1)
]

for origem, destino, peso in arestas:
    g.adicionar_aresta(origem, destino, peso)



g.exibir_grafo_matriz()
g.prim()


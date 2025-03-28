import time


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

        print("""
        
        ------------------------------------------
        Arestas da Árvore Geradora Mínima:
        """)
        custo_total = 0
        for i in range(1, self.V):
            origem = self.bairros[pai[i]]
            destino = self.bairros[i]
            print(f"{origem} - {destino} (Peso: {self.grafo[i][pai[i]]})")
            custo_total += self.grafo[i][pai[i]]
        print(f"\nPeso total da AGM: {custo_total}")


print("""------------------------------------------
Exercício 1.2 - Algoritmo de prim (Àrvore geradora mínima)
------------------------------------------""")


def testar_prim(bairros, arestas):
    g = PrimGrafoFibraOtica(bairros)

    for origem, destino, peso in arestas:
        g.adicionar_aresta(origem, destino, peso)
    inicio = time.time()
    g.prim()
    duracao = time.time() - inicio
    print(f"""Tempo de execução para
     o algoritmo de prim encontrar a 
     minima árvore geradora: {duracao:.12f} segundos""")


bairros = ["Copacabana", "Ipanema", "Leblon", "Botafogo", "Tijuca", "Centro"]
arestas = [
    ("Copacabana", "Ipanema", 4), ("Copacabana", "Leblon", 2), ("Ipanema", "Leblon", 5),
    ("Ipanema", "Botafogo", 10), ("Leblon", "Botafogo", 8), ("Leblon", "Tijuca", 3),
    ("Botafogo", "Tijuca", 7), ("Botafogo", "Centro", 6), ("Tijuca", "Centro", 1)
]
testar_prim(bairros, arestas)

print("\nTestando com bairros de São Paulo....")

bairros_sp = [
    "Pinheiros", "Vila Madalena", "Jardins", "Bela Vista", "Consolação", "Sé",
    "Moema", "Itaim Bibi", "Brooklin", "Santana", "Tatuapé", "Liberdade"
]

arestas_sp = [
    ("Pinheiros", "Vila Madalena", 3), ("Pinheiros", "Jardins", 4), ("Vila Madalena", "Jardins", 2),
    ("Jardins", "Bela Vista", 6), ("Bela Vista", "Consolação", 1), ("Consolação", "Sé", 5),
    ("Sé", "Liberdade", 3), ("Sé", "Bela Vista", 2), ("Liberdade", "Tatuapé", 7),
    ("Tatuapé", "Santana", 8), ("Santana", "Consolação", 9), ("Moema", "Itaim Bibi", 2),
    ("Itaim Bibi", "Brooklin", 3), ("Brooklin", "Moema", 4), ("Brooklin", "Vila Madalena", 6),
    ("Moema", "Pinheiros", 7), ("Bela Vista", "Itaim Bibi", 5), ("Liberdade", "Brooklin", 8)
]

testar_prim(bairros_sp, arestas_sp)


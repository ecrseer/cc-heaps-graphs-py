def organiza_mochila(capacidade, pesos, valores, n):

    matriz_capaci = [[0 for _ in range(capacidade + 1)] for _ in range(n + 1)]


    for i in range(1, n + 1):
        for w in range(capacidade + 1):
            max_peso_possivel = pesos[i - 1] <= w
            if max_peso_possivel:
                matriz_capaci[i][w] = max(valores[i - 1] + matriz_capaci[i - 1][w - pesos[i - 1]], matriz_capaci[i - 1][w])
            else:
                matriz_capaci[i][w] = matriz_capaci[i - 1][w]

    return matriz_capaci[n][capacidade]


def exercicio61():
    pesos1 = [2, 3, 4, 5]
    valores1 = [3, 4, 5, 6]
    capacidade1 = 5
    n1 = len(pesos1)
    pesos2 = [1, 2, 3, 8, 7, 4]
    valores2 = [20, 5, 10, 40, 15, 25]
    capacidade2 = 10
    n2 = len(pesos2)

    print(f"Valor máximo para o primeiro conjunto: {organiza_mochila(capacidade1, pesos1, valores1, n1)}")
    print(f"Valor máximo para o segundo conjunto: {organiza_mochila(capacidade2, pesos2, valores2, n2)}")


exercicio61()

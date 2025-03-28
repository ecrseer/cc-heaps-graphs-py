def mochila_gulosa(capacidade, itens):
    itens.sort(key=lambda x: x[1] / x[0], reverse=True)

    valor_total = 0
    peso_atual = 0
    itens_selecionados = []

    for peso, valor in itens:
        if peso_atual + peso <= capacidade:
            peso_atual += peso
            valor_total += valor
            itens_selecionados.append((peso, valor))

    return valor_total, itens_selecionados


def executar_mochila_gulosa(capacidade, itens):
    valor_maximo, itens_usados = mochila_gulosa(capacidade, itens)

    print("\nItens selecionados para a mochila:")
    for i, (peso, valor) in enumerate(itens_usados, start=1):
        print(f"item{i}: peso {peso}, valor {valor}")

    print(f"\nCapacidade da mochila: {capacidade}")
    print(f"Valor máximo possível na mochila: {valor_maximo}")



itens = [(2, 40), (3, 50), (5, 100), (4, 90)]
capacidade = 8


executar_mochila_gulosa(capacidade, itens)

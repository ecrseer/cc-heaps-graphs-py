import time

movimentos = [
    (2, 1), (2, -1), (-2, 1), (-2, -1),
    (1, 2), (1, -2), (-1, 2), (-1, -2)
]


def dentro_tabuleiro(x, y, dimXdim):
    return 0 <= x < dimXdim and 0 <= y < dimXdim


def passeio_cavalo_forca_bruta(tabuleiro, x, y, move_count, dimXdim):
    todos_visitados = move_count == dimXdim * dimXdim
    if todos_visitados:
        return True

    for dx, dy in movimentos:
        nx, ny = x + dx, y + dy
        print(f"nx: {nx}, ny: {ny}")
        if dentro_tabuleiro(nx, ny, dimXdim) and tabuleiro[nx][ny] == -1:
            tabuleiro[nx][ny] = move_count
            if passeio_cavalo_forca_bruta(tabuleiro, nx, ny, move_count + 1, dimXdim):
                return True
            tabuleiro[nx][ny] = -1  # Backtrack

    return False


def resolver_passeio_cavalo(dimXdim, inicio_x=0, inicio_y=0):
    tabuleiro = [[-1] * dimXdim for _ in range(dimXdim)]
    tabuleiro[inicio_x][inicio_y] = 0

    if not passeio_cavalo_forca_bruta(tabuleiro, inicio_x, inicio_y, 1, dimXdim):
        print("Falha: Nenhuma solução encontrada!")
        return None

    return tabuleiro


def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" ".join(f"{num:2}" for num in linha))


inicio = time.time()
N = 5
solucao = resolver_passeio_cavalo(N)
if solucao:
    print("\nPasseio do Cavalo encontrado (Força Bruta):")
    imprimir_tabuleiro(solucao)
    print(f"Tempo de execução: {time.time() - inicio:.12f} milisegundos.")

# Definição dos possíveis movimentos do cavalo
import time

movimentos = [
    (2, 1), (2, -1), (-2, 1), (-2, -1),
    (1, 2), (1, -2), (-1, 2), (-1, -2)
]


def dentro_tabuleiro(x, y, dimXdim):
    # Verifica se a posição está dentro dos limites do tabuleiro.
    return 0 <= x < dimXdim and 0 <= y < dimXdim


def movimentos_possiveis(tabuleiro, x, y, dimXdim):
    # Retorna a lista de movimentos válidos a partir de (x, y).
    moves = []
    for dx, dy in movimentos:
        print(f"dx: {dx}, dy: {dy}")
        nx, ny = x + dx, y + dy
        if dentro_tabuleiro(nx, ny, dimXdim) and tabuleiro[nx][ny] == -1:
            moves.append((nx, ny))
    return moves


def proximo_movimento(tabuleiro, x, y, dimXdim):
    # Escolhe o próximo movimento com base na heurística de Warnsdorff.
    moves = movimentos_possiveis(tabuleiro, x, y, dimXdim)
    if not moves:
        return None

    # Ordena os movimentos pelo número de opções futuras (Warnsdorff)
    moves.sort(key=lambda move: len(movimentos_possiveis(tabuleiro, move[0], move[1], dimXdim)))

    return moves[0]  # Retorna o movimento com menos opções futuras


def passeio_do_cavalo(altXlarg, inicio_x=0, inicio_y=0):
    # Resolve o problema do passeio do cavalo usando a heurística de Warnsdorff.
    tabuleiro = [[-1] * altXlarg for _ in range(altXlarg)]
    x, y = inicio_x, inicio_y
    tabuleiro[x][y] = 0  # Posição inicial do cavalo

    for i in range(1, altXlarg * altXlarg):
        movimento = proximo_movimento(tabuleiro, x, y, altXlarg)
        if not movimento:
            print("Falha: Caminho interrompido!")
            return None

        x, y = movimento
        tabuleiro[x][y] = i  # Marca o movimento no tabuleiro

    return tabuleiro


def imprimir_tabuleiro(tabuleiro):
    # Imprime o tabuleiro formatado.
    for linha in tabuleiro:
        print(" ".join(f"{num:2}" for num in linha))


inicio = time.time()
N = 5  # Tabuleiro 8x8
solucao = passeio_do_cavalo(N)

if solucao:
    print("\nPasseio do Cavalo encontrado:")
    imprimir_tabuleiro(solucao)
    print(f"Tempo de execução: {time.time() - inicio:.12f} milisegundos.")

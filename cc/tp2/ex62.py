def sequencia_texto_entre(seq1, seq2):
    m, n = len(seq1), len(seq2)

    matriz_text = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if seq1[i - 1] == seq2[j - 1]:
                matriz_text[i][j] = matriz_text[i - 1][j - 1] + 1
            else:
                matriz_text[i][j] = max(matriz_text[i - 1][j], matriz_text[i][j - 1])

    lcs_length = matriz_text[m][n]
    i, j = m, n
    lcs_seq = []
    while i > 0 and j > 0:
        if seq1[i - 1] == seq2[j - 1]:
            lcs_seq.append(seq1[i - 1])
            i -= 1
            j -= 1
        elif matriz_text[i - 1][j] > matriz_text[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return lcs_length, "".join(reversed(lcs_seq))  # Revertendo para obter na ordem correta


def exercicio62():
    seq1 = "ABCBDAB"
    seq2 = "BDCAB"

    seq3 = "AGGTAB"
    seq4 = "GXTXAYB"

    length1, lcs1 = sequencia_texto_entre(seq1, seq2)
    length2, lcs2 = sequencia_texto_entre(seq3, seq4)

    print(f"LCS entre '{seq1}' e '{seq2}': '{lcs1}' (comprimento {length1})")
    print(f"LCS entre '{seq3}' e '{seq4}': '{lcs2}' (comprimento {length2})")


exercicio62()
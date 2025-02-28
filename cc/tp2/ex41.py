def calc_fatorial_de(numero):
    if numero == 0:
        return 1
    else:
        return numero * calc_fatorial_de(numero - 1)


def exercicio41():
    print("Fatorial de 5: ", calc_fatorial_de(5))


if __name__ == "__main__":
    exercicio41()

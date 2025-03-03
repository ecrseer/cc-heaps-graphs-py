import time


def fibonacci_memoizado(n, memo):
    if memo is None:
        memo = {}

    if n == 0:
        return 0
    if n == 1:
        return 1

    if n in memo:
        return memo[n]

    memo[n] = fibonacci_memoizado(n - 1, memo) + fibonacci_memoizado(n - 2, memo)
    return memo[n]


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    kesimo = fibonacci(n - 1) + fibonacci(n - 2)
    return kesimo;


def exercicio42(k=7):
    inicio = time.time()
    print(f"Fibonacci de {k - 1}-esimo numero: ", fibonacci(k))
    print(f"Tempo para calcular fibonacci sem memoização: {time.time() - inicio:.6f}")

    inicio2 = time.time()
    print(f"Fibonacci de {k - 1}-esimo numero: ", fibonacci_memoizado(k, {}))
    print(f"Tempo para calcular fibonacci com memoização: { time.time() - inicio2:.6f}")


if __name__ == "__main__":
    exercicio42()

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


def exercicio42():
    print("Fibonacci de 3: ", fibonacci_memoizado(3, {}))


if __name__ == "__main__":
    exercicio42()
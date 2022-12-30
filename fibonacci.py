def fibonacci_recur(n):
    assert n >= 0, "n > 0"
    if n <= 1:
        return n
    if n == 2:
        return fibonacci_recur(n - 1)
    else:
        return fibonacci_recur(n - 1) + fibonacci_recur(n - 2)


for i in range(1, 20):
    print(fibonacci_recur(i), end=' ')

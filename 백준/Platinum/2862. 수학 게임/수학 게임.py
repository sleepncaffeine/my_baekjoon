def zeckendorf(n):
    # Generate Fibonacci sequence up to n
    fibo = [1, 1]
    while fibo[-1] <= n:
        fibo.append(fibo[-1] + fibo[-2])

    # Zeckendorf representation
    last_fib = None
    for i in range(len(fibo) - 1, -1, -1):
        if fibo[i] <= n:
            last_fib = fibo[i]
            n -= last_fib

    return last_fib


n = int(input())
result = zeckendorf(n)
print(result)

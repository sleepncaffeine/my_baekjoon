def isprime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def dfs(n, d):
    if d == N:
        print(n)
        return
    for i in range(1, 10):
        if isprime(n * 10 + i):
            dfs(n * 10 + i, d + 1)


N = int(input())

for i in range(2, 10):
    if isprime(i):
        dfs(i, 1)

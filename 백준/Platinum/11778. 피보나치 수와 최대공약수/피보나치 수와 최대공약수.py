import math

MOD = 10**9 + 7

memo = {
    1: 1,
    2: 1,
    3: 2,
    4: 3,
    5: 5,
}


def fib(n):
    if n in memo:
        return memo[n]
    if n % 2 == 0:
        memo[n] = (fib(n + 1) - fib(n - 1)) % MOD
    else:
        memo[n] = (fib(n // 2) ** 2 + fib(n // 2 + 1) ** 2) % MOD

    return memo[n]


n, m = map(int, input().split())
print(fib(math.gcd(n, m)))

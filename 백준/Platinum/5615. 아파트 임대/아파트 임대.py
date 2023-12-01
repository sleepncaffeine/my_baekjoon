import sys

input = sys.stdin.readline


def powermod(a, b, m):
    res = 1
    a %= m
    while b > 0:
        if b & 1:
            res = (res * a) % m
        a = (a * a) % m
        b //= 2
    return res


def miller_rabin(n, a):
    d = n - 1
    while d % 2 == 0:
        if powermod(a, d, n) == n - 1:
            return True
        d //= 2
    r = powermod(a, d, n)
    return r == n - 1 or r == 1


def is_prime(n):
    if n == 1 or n % 2 == 0:
        return False
    for a in [2, 7, 61]:
        if n == a:
            return True
        if not miller_rabin(n, a):
            return False
    return True


n = int(input())
cnt = 0
for _ in range(n):
    a = int(input())
    if is_prime(2 * a + 1):
        cnt += 1
print(cnt)

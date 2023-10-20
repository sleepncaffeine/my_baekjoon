import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** (1 / 2)) + 1):
        if not n % i:
            return False
    return True


def dfs(n, cnt):
    if cnt == N:
        print(n)
        return
    for i in range(1, 10):
        if is_prime(n * 10 + i):
            dfs(n * 10 + i, cnt + 1)


N = int(input())

for i in range(1, 10):
    if is_prime(i):
        dfs(i, 1)

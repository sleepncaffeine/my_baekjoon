import sys
import random

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())


def pow(a, b, c):
    res = 1
    a %= c
    while b > 0:
        if b % 2 == 1:
            res = res * a % c
        a = a * a % c
        b //= 2
    return res


def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def miller_rabin(n, k):
    r = 0
    d = n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    x = pow(k, d, n)
    if x == 1 or x == n - 1:
        return True

    for i in range(r - 1):
        x = x * x % n
        if x == n - 1:
            return True
    return False


def is_prime(n):
    plist = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    if n <= 1:
        return False
    for p in plist:
        if n == p:
            return True
        if not miller_rabin(n, p):
            return False
    return True


def pollard_rho(n):
    if is_prime(n):
        return n
    if n % 2 == 0:
        return 2
    x = random.randint(2, n)
    y = x
    c = random.randint(1, n)
    d = 1
    while d == 1:
        x = (x * x + c) % n
        y = (y * y + c) % n
        y = (y * y + c) % n
        d = gcd(abs(x - y), n)
        if d == n:
            return pollard_rho(n)
    if is_prime(d):
        return d
    else:
        return pollard_rho(d)


arr = []

while n > 1:
    p = pollard_rho(n)
    arr.append(p)
    n //= p

arr.sort()
for i in arr:
    print(i)
import sys
from math import gcd, sqrt
from random import randrange
from collections import Counter

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
    for a in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]:
        if n == a:
            return True
        if not miller_rabin(n, a):
            return False
    return True

def pollard_rho(n):
    if is_prime(n):
        return n
    if n == 1:
        return 1
    if n % 2 == 0:
        return 2
    
    x = randrange(2, n)
    y = x
    c = randrange(1, n)
    g = 1
    while g == 1:
        x = (x * x % n + c + n) % n
        y = (y * y % n + c + n) % n
        y = (y * y % n + c + n) % n
        g = gcd(abs(x - y), n)

        if g == n:
            return pollard_rho(n)
        
    return pollard_rho(g)

def quad(n):
    while n % 4 == 0:
        n //= 4
    return n % 8 == 7

def cube(n):
    l = []
    while n > 1:
        p = pollard_rho(n)
        l.append(p)
        n //= p
    c = list(Counter(l).items())
    for p, e in c:
        if p % 4 == 3 and e % 2 == 1:
            return True
    return False

def solve(n):
    if quad(n):
        return 4
    elif cube(n):
        return 3
    elif int(sqrt(n)) ** 2 != n:
        return 2
    else:
        return 1

input = sys.stdin.readline
res = solve(int(input()))
print(res)
import sys
from math import gcd
from random import randrange

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

n = int(sys.stdin.readline())

if n == 1:
    print(1)
    exit()

anslist = []
while n != 1:
    anslist.append(pollard_rho(n))
    n //= anslist[-1]

anslist.sort()
ans, mul = 1, 2
for i in range(len(anslist) - 1):
    if(anslist[i] == anslist[i + 1]):
        mul += 1
    else:
        ans *= mul
        mul = 2
ans *= mul
print(ans)
def modp(n, r, p):
    C = [0] * (r + 1)
    C[0] = 1

    for i in range(1, n + 1):
        for j in range(min(i, r), 0, -1):
            C[j] = (C[j] + C[j - 1]) % p
    return C[r]


def ncr(n, r, p):
    if r == 0:
        return 1
    ni = n % p
    ri = r % p
    return (ncr(n // p, r // p, p) * modp(ni, ri, p)) % p


n, r, p = map(int, input().split())
print(ncr(n, r, p))

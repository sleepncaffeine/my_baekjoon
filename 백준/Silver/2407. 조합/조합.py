n, r = map(int, input().split())

memo = {}


def ncr(n, r):
    if r == 0 or r == n:
        return 1
    if r == 1:
        return n
    if (n, r) in memo:
        return memo[(n, r)]
    memo[(n, r)] = ncr(n - 1, r - 1) + ncr(n - 1, r)
    return memo[(n, r)]


print(ncr(n, r))

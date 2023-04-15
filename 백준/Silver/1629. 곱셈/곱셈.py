def div_con_pow(x, y, z):
    res = 1
    while y:
        if y & 1:
            res *= x
        x *= x
        x %= z
        y >>= 1
    return res % z


a, b, c = map(int, input().split())

print(div_con_pow(a, b, c))

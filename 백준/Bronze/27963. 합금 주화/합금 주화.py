d1, d2, x = map(int, input().split())
if d1 > d2:
    d1, d2 = d2, d1
p = (100 - x) / x
ans = (p + 1) / (p * d2 / d1 + 1) * d2
print(ans)

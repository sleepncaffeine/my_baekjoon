n = int(input())
ans = 0

for i in range(2, n // 2 + 1):
    tmp = n // i
    ans += (tmp - 1) * i

print(ans % 1000000)

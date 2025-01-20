n = int(input())

MAXI = 10000
res = MAXI
for _ in range(n):
    arrive, open_t = map(int, input().split())
    if open_t < arrive:
        continue

    if open_t < res:
        res = open_t

if res == MAXI:
    print(-1)
else:
    print(res)

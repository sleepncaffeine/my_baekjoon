n = int(input())
stones = list(map(int, input().split()))

x = 0

for stone in stones:
    x ^= stone

if x:
    print("koosaga")
else:
    print("cubelover")

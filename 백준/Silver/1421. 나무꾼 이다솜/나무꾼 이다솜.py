from math import ceil

n, c, w = map(int, input().split())
trees = []
for _ in range(n):
    trees.append(int(input()))

profit = []

for l in range(1, max(trees) + 1):
    tsum = 0
    for t in trees:
        if t % l == 0:
            cut = t // l - 1
        else:
            cut = t // l
        tsum += max(0, w * l * (t // l) - c * cut)
    profit.append(tsum)

print(max(profit) if profit else 0)

n = int(input())

pos = []
neg = []
res = 0

for _ in range(n):
    num = int(input())
    if num > 1:
        pos.append(num)
    elif num <= 0:
        neg.append(num)
    else:
        res += num

pos.sort(reverse=True)
neg.sort()

for i in range(0, len(pos), 2):
    if i + 1 < len(pos):
        res += pos[i] * pos[i + 1]
    else:
        res += pos[i]


for i in range(0, len(neg), 2):
    if i + 1 < len(neg):
        res += neg[i] * neg[i + 1]
    else:
        res += neg[i]

print(res)
s = input()
res = []

for i in range(26):
    ch = chr(ord("a") + i)
    cnt = s.count(ch)
    res.append(cnt)

print(*res)

a = int(input())
title = []
diff = []

for i in range(a):
    n, m = input().split()
    title.append(n)
    diff.append(m)

for i in range(len(diff)):
    if diff[i] == min(diff):
        print(title[i])

from collections import deque

n = int(input())
a = list(map(int, input().split()))

q = deque()
ans = [-1] * n
for i in range(n):
    while q and a[q[-1]] < a[i]:
        ans[q.pop()] = a[i]
    q.append(i)

for i in ans:
    print(i, end=" ")

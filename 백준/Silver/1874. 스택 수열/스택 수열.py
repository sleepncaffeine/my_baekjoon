from collections import deque

n = int(input())

a = []
for _ in range(n):
    a.append(int(input()))

q = deque()
ans = []
for i in range(1, n + 1):
    q.append(i)
    ans.append("+")
    while q and q[-1] == a[0]:
        q.pop()
        a.pop(0)
        ans.append("-")

if a:
    print("NO")
else:
    for i in ans:
        print(i)
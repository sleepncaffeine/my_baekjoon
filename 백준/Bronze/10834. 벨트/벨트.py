m = int(input())
ans = 0
rot = 0
for i in range(m):
    a, b, s = map(int, input().split())
    if i == 0:
        ans = a * b
    else:
        ans = int(ans / a * b)
    if s == 1:
        rot = 1 - rot

print(rot,ans)
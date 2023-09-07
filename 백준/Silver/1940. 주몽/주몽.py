# 007
# boj 1940
# acmicpc.net/problem/1940

n = int(input())
m = int(input())
a = list(map(int, input().split()))

a.sort()
ans = 0

s = 0
e = n - 1
    
while s < e:
    sum = a[s] + a[e]
    if sum == m:
        ans += 1
        s += 1
        e -= 1
    elif sum < m:
        s += 1
    else:
        e -= 1

print(ans)

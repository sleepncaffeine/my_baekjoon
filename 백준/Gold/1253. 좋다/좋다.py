n = int(input())
a = list(map(int, input().split()))
a.sort()

ans = 0

for i in range(n):
    s = 0
    e = n - 1
    while s < e:
        if s == i:
            s += 1
            continue
        if e == i:
            e -= 1
            continue
        sum = a[s] + a[e]
        if sum == a[i]:
            ans += 1
            break
        elif sum < a[i]:
            s += 1
        else:
            e -= 1

print(ans)

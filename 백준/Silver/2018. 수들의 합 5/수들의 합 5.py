n = int(input())
ans = 0
s = 1
e = 1
sum = 1

while s <= n:
    if sum == n:
        ans += 1
        sum -= s
        s += 1
    elif sum < n:
        e += 1
        sum += e
    else:
        sum -= s
        s += 1

print(ans)
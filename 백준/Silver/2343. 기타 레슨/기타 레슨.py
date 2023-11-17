n, m = map(int, input().split())
lens = list(map(int, input().split()))

l = max(lens)
r = sum(lens)

while l <= r:
    mid = (l + r) // 2
    cnt = 0
    tmp = 0
    for i in lens:
        if tmp + i > mid:
            cnt += 1
            tmp = 0
        tmp += i
    else:
        if tmp:
            cnt += 1

    if cnt <= m:
        r = mid - 1
    else:
        l = mid + 1

print(l)
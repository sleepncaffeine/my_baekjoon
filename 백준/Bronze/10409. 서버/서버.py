n, t = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0

for i in arr:
    if i <= t:
        t -= i
        cnt += 1
    else:
        break

print(cnt)

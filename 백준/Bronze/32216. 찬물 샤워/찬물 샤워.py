n, k, t = map(int, input().split())
d = [0] + list(map(int, input().split()))
arr = [t] + [0] * n

for i in range(n):
    if arr[i] > k:
        arr[i + 1] = arr[i] + d[i + 1] - abs(arr[i] - k)
    elif arr[i - 1] < k:
        arr[i + 1] = arr[i] + d[i + 1] + abs(arr[i] - k)
    else:
        arr[i + 1] = arr[i] + d[i + 1]

ans = 0
for t in arr[1:]:
    ans += abs(t - k)

print(ans)

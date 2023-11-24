n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

arr.sort(key=lambda x: (x[1], x[0]))

cnt = 0
end = 0

for a in arr:
    if a[0] >= end:
        cnt += 1
        end = a[1]

print(cnt)

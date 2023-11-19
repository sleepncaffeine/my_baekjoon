import sys

input = sys.stdin.readline

n = int(input())
cnt = 0
arr = []
for _ in range(n):
    sm, sd, em, ed = map(int, input().split())
    arr.append((sm * 100 + sd, em * 100 + ed))
arr.sort()

end = 301
LAST = 1201

while arr:
    if arr[0][0] > end:
        break
    if end >= LAST:
        break

    tmp = -1

    for _ in range(len(arr)):
        if arr[0][0] <= end:
            if tmp < arr[0][1]:
                tmp = arr[0][1]

            arr.pop(0)
        else:
            break

    end = tmp
    cnt += 1

if end >= LAST:
    print(cnt)
else:
    print(0)

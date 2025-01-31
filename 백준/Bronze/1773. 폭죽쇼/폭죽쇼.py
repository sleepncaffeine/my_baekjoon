import sys

input = sys.stdin.readline


n, c = map(int, input().split())
arr = [0] * (2000001)

for _ in range(n):
    t = int(input())
    tmp = t
    while True:
        if tmp <= c:
            arr[tmp] = 1
            tmp += t
        else:
            break

print(sum(arr))

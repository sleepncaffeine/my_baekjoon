import sys

input = sys.stdin.readline

n = int(input())
arr = []

for i in range(n):
    arr.append((int(input()), i))

max = 0
arr.sort()

for i in range(n):
    if max < arr[i][1] - i:
        max = arr[i][1] - i

print(max + 1)

import sys

print = sys.stdout.write

n, k = map(int, input().split())

arr = list(map(int, input().split()))

arr.sort()

print(str(arr[k - 1]))
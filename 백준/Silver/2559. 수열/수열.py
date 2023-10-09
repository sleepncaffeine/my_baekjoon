import sys

input = sys.stdin.readline
print = sys.stdout.write

n, k = map(int, input().split())
temps = list(map(int, input().split()))
prefix_sum = []

for i in range(n):
    if i == 0:
        prefix_sum.append(temps[i])
    else:
        prefix_sum.append(prefix_sum[i - 1] + temps[i])

max_sum = 0

for i in range(n - k + 1):
    if i == 0:
        max_sum = prefix_sum[i + k - 1]
    else:
        max_sum = max(max_sum, prefix_sum[i + k - 1] - prefix_sum[i - 1])

print(str(max_sum))

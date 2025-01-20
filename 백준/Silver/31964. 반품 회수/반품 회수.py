import sys

input = sys.stdin.readline


n = int(input())
x = list(map(int, input().split()))
t = list(map(int, input().split()))

ret = x[n - 1]

for i in range(n - 1, -1, -1):  # for (int i = n - 1 ; i >= 0 ; --i)
    if i != n - 1:
        ret += x[i + 1] - x[i]

    if ret < t[i]:
        ret = t[i]

ret += x[0]

print(ret)

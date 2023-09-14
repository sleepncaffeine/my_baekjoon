import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

stack = []
ans = [0] * n

for i in range(n):
    while stack and a[stack[-1]] < a[i]:
        stack.pop()
    if stack:
        ans[i] = stack[-1] + 1
    stack.append(i)

print(*ans)

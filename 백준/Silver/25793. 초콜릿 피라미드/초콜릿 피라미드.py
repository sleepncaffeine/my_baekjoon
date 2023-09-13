import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    r, c = map(int, input().rstrip().split())
    if r > c:
        r, c = c, r
    k = c - r
    white = r * (r + 1) * (2 * r + 1) // 3 - r * (r + 1) + r * (r + 1) * k - r * k + r
    black = r * (r + 1) * (2 * r + 1) // 3 - r * (r + 1) + r * (r + 1) * k - r * k
    print(white, black)

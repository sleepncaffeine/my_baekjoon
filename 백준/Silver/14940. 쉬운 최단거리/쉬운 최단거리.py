import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
space = []
q = deque([])
visited = [[0] * m for _ in range(n)]
res = [[-1] * m for _ in range(n)]

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(m):
        if row[j] == 2:
            q.append((i, j))
            visited[i][j] = 1
            res[i][j] = 0
        elif row[j] == 0:
            res[i][j] = 0
    space.append(row)

dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
while q:
    x, y = q.popleft()
    for dx, dy in dir:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and space[nx][ny] == 1:
            visited[nx][ny] = 1
            res[nx][ny] = res[x][y] + 1
            q.append((nx, ny))

for i in range(n):
    for j in range(m):
        print(res[i][j], end=" ")
    print()

import sys
from collections import deque

input = sys.stdin.readline


def bfs(g, s):
    visited = [[False] * m for _ in range(n)]
    visited[s[0]][s[1]] = True
    q = deque([s])

    while q:
        a, b = q.popleft()
        for x, y in [(a - 1, b), (a + 1, b), (a, b - 1), (a, b + 1)]:
            if 0 <= x < n and 0 <= y < m and g[x][y] and not visited[x][y]:
                visited[x][y] = True
                g[x][y] = g[a][b] + 1
                q.append((x, y))


n, m = map(int, input().split())
maze = []
for _ in range(n):
    maze.append(list(map(int, input().strip())))

bfs(maze, (0, 0))

print(maze[n - 1][m - 1])

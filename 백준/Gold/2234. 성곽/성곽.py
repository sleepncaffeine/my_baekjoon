from collections import deque

n, m = map(int, input().split())
castle = [list(map(int, input().split())) for _ in range(m)]

visited = [[False] * n for _ in range(m)]

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

room_cnt = 0
room_size = []
max_room_size = 0

for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            room_cnt += 1
            q = deque([(i, j)])
            visited[i][j] = True
            size = 1
            while q:
                x, y = q.popleft()
                for k in range(4):
                    if not castle[x][y] & (1 << k):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                            visited[nx][ny] = True
                            q.append((nx, ny))
                            size += 1
            room_size.append(size)
            max_room_size = max(max_room_size, size)

print(room_cnt)
print(max_room_size)

max_room_size = 0
for i in range(m):
    for j in range(n):
        for k in range(4):
            if castle[i][j] & (1 << k):
                visited = [[False] * n for _ in range(m)]
                castle[i][j] -= 1 << k
                q = deque([(i, j)])
                visited[i][j] = True
                size = 1
                while q:
                    x, y = q.popleft()
                    for l in range(4):
                        if not castle[x][y] & (1 << l):
                            nx = x + dx[l]
                            ny = y + dy[l]
                            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                                visited[nx][ny] = True
                                q.append((nx, ny))
                                size += 1
                castle[i][j] += 1 << k
                max_room_size = max(max_room_size, size)

print(max_room_size)
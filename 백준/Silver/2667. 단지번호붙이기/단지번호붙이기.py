graph = []
num = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())

for i in range(n):
    graph.append(list(map(int, input())))


def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if graph[x][y] == 1:
        global cnt
        cnt += 1
        graph[x][y] = 0
        for i in range(4):
            dfs(x + dx[i], y + dy[i])
        return True
    return False


res = 0
cnt = 0

for i in range(n):
    for j in range(n):
        if dfs(i, j):
            res += 1
            num.append(cnt)
            cnt = 0

num.sort()
print(res)
for i in num:
    print(i)

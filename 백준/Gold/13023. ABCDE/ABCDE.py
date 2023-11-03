n, m = map(int, input().split())
graph = [[] for _ in range(n)]
visited = [False] * 2001

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(i, d):
    global ans
    visited[i] = True
    if d == 4:
        ans = True
        return
    for j in graph[i]:
        if not visited[j]:
            dfs(j, d + 1)
            visited[j] = False


ans = False
for i in range(n):
    dfs(i, 0)
    visited[i] = False
    if ans:
        break

print(1 if ans else 0)
n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(v):
    visited[v] = True
    print(v, end=" ")
    for i in sorted(graph[v]):
        if not visited[i]:
            dfs(i)


def bfs(v):
    visited[v] = True
    queue = [v]
    while queue:
        v = queue.pop(0)
        print(v, end=" ")
        for i in sorted(graph[v]):
            if not visited[i]:
                queue.append(i)
                visited[i] = True


visited = [False] * (n + 1)
dfs(v)
print()
visited = [False] * (n + 1)
bfs(v)

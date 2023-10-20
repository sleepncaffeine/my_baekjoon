import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)


dfs(1)
print(visited.count(True) - 1)
import sys
from collections import deque

input = sys.stdin.readline


def dfs(g, s):
    visited = [False] * (n + 1)
    visited[s] = True
    stack = [s]
    max_dist = [0] * (n + 1)

    while stack:
        v = stack.pop()
        for i in g[v]:
            if not visited[i[0]]:
                visited[i[0]] = True
                stack.append(i[0])
                max_dist[i[0]] = max_dist[v] + i[1]

    return max_dist


n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n):
    a = list(map(int, input().split()))
    for i in range(1, len(a) - 1, 2):
        graph[a[0]].append((a[i], a[i + 1]))

max_dist = dfs(graph, 1)

max_idx = max_dist.index(max(max_dist))
max_dist = dfs(graph, max_idx)

print(max(max_dist))

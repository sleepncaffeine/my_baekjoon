import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(s, t, v):
    for n, w in t[s]:
        if not v[n]:
            v[n] = v[s] + w
            dfs(n, t, v)


n = int(input())
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    p, c, w = map(int, input().split())
    tree[p].append((c, w))
    tree[c].append((p, w))

visited = [0] * (n + 1)
dfs(1, tree, visited)
visited[1] = 0
max_ = visited.index(max(visited))
visited = [0] * (n + 1)
dfs(max_, tree, visited)
visited[max_] = 0
print(max(visited))

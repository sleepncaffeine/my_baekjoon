import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(x):
    for i in tree[x]:
        if parent[i] == 0:
            parent[i] = x
            dfs(i)


n = int(input())
tree = [[] for _ in range(n + 1)]
parent = [0] * (n + 1)

for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

dfs(1)

for i in range(2, n + 1):
    print(parent[i])

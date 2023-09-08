import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)


def dijkstra(start):
    q = []
    distance = [INF] * (v + 1)

    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if dist > distance[now]:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return distance


v, e, x = map(int, input().split())
graph = [[] for _ in range(v + 1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

result = 0

for i in range(1, v + 1):
    if i == x:
        continue

    distance = dijkstra(i)
    result = max(result, distance[x] + dijkstra(x)[i])

print(result)

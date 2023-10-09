import sys

input = sys.stdin.readline

INF = 1234567890


def b_f(N, road):
    D = [INF] * (N + 1)
    D[1] = 0

    for i in range(N):
        for r in road:
            s, e, t = r
            if D[e] > D[s] + t:
                D[e] = D[s] + t
                if i == N - 1:
                    return True
    return False


T = int(input())

for _ in range(T):
    n, m, w = map(int, input().split())
    road = []

    for _ in range(m):
        s, e, t = map(int, input().split())
        road.append([s, e, t])
        road.append([e, s, t])

    for _ in range(w):
        s, e, t = map(int, input().split())
        road.append([s, e, -t])

    if b_f(n, road):
        print("YES")
    else:
        print("NO")

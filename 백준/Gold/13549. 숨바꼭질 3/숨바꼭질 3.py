from collections import deque


def bfs(n):
    visited = [0] * 100001
    dq = deque()
    dq.append(n)
    while dq:
        pos = dq.popleft()
        if pos == k:
            return visited[pos]
        for next_pos in (pos + 1, pos - 1, pos * 2):
            if 0 <= next_pos <= 100000 and visited[next_pos] == 0:
                if next_pos == pos * 2 and next_pos != 0:
                    visited[next_pos] = visited[pos]
                    dq.appendleft(next_pos)
                else:
                    visited[next_pos] = visited[pos] + 1
                    dq.append(next_pos)


n, k = map(int, input().split())
print(bfs(n))

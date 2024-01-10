from collections import deque

n, k = map(int, input().split())
visited = [0] * 100001
q = deque()
q.append(n)
visited[n] = 1

while q:
    x = q.popleft()
    if x == k:
        print(visited[x] - 1)
        break
    for i in (x - 1, x + 1, x * 2):
        if 0 <= i <= 100000 and visited[i] == 0:
            if i == x * 2:
                visited[i] = visited[x]
                q.appendleft(i)
            else:
                visited[i] = visited[x] + 1
                q.append(i)
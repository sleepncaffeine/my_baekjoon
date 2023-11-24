from heapq import heappush, heappop

n = int(input())
heap = []

for _ in range(n):
    heappush(heap, int(input()))

ans = 0
while len(heap) > 1:
    a = heappop(heap)
    b = heappop(heap)
    ans += a + b
    heappush(heap, a + b)

print(ans)

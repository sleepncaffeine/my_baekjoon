n, x = map(int, input().split())


bus = []
for _ in range(n):
    s, t = map(int, input().split())
    if s + t <= x:
        bus.append(s)

if bus:
    bus.sort()
    print(bus[-1])
else:
    print(-1)

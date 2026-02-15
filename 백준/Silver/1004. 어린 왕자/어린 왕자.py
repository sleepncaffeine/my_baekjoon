def dist2(x1, y1, x2, y2):
    return (x1 - x2) ** 2 + (y1 - y2) ** 2


t = int(input())
for _ in range(t):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    planets = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for x, y, r in planets:
        d1 = dist2(x1, y1, x, y)
        d2 = dist2(x2, y2, x, y)
        r2 = r**2
        if (d1 < r2 and d2 >= r2) or (d1 >= r2 and d2 < r2):
            ans += 1

    print(ans)

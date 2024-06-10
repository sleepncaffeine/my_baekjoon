def check(radii):
    radii.sort()

    for i in range(1, len(radii)):
        if sum(radii[:i]) >= radii[i]:
            return "YES"
    return "NO"


t = int(input())
for _ in range(t):
    K = int(input())
    radii = list(map(float, input().strip().split()))
    print(check(radii))

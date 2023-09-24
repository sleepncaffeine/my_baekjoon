n = int(input())
x, y, r = map(int, input().split())
right_end = x + r
left_end = x - r
T = []
for i in range(n):
    T.append(int(input()))

inside = 0
edge = 0
for t in T:
    if left_end < t < right_end:
        inside += 1
    elif t == left_end or t == right_end:
        edge += 1

print(inside, edge)
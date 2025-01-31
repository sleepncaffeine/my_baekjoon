import sys

input = sys.stdin.readline

cnt_a = cnt_b = 0
for _ in range(int(input())):
    a, b = map(int, input().split())
    if a > b:
        cnt_a += 1
    elif a < b:
        cnt_b += 1
print(cnt_a, cnt_b)

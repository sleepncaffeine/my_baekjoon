n, x = map(int, input().split())
a = list(map(int, input().split()))

sum_a = sum(a)

if sum_a % x == 0:
    print(1)
else:
    print(0)
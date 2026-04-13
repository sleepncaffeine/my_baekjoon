l, p = map(int, input().split())
nums = list(map(int, input().split()))
x = l * p
print(*[n - x for n in nums])

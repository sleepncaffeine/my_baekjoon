numbers = list(map(int, input().split()))
pn = map(lambda x: x**2, numbers)
print(sum(pn)%10)
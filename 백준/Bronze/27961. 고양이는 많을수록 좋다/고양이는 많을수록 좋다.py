import math

n = int(input())

if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    res = math.ceil(round(math.log(n, 2), 10))
    print(res + 1)

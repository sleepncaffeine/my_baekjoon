ans = 1
tmp = 1
n = int(input())

if n % 2 == 0 or n % 5 == 0:
    print(-1)
    exit()
while (tmp % n) != 0:
    tmp = (tmp % n) * 10 + 1
    ans += 1
print(ans)

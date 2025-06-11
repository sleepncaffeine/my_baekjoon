Q = 25
D = 10
N = 5
P = 1

n = int(input())
for _ in range(n):
    price = int(input())
    coins = []
    coins.append(price // Q)
    price %= Q
    coins.append(price // D)
    price %= D
    coins.append(price // N)
    price %= N
    coins.append(price // P)
    price %= P
    print(*coins)

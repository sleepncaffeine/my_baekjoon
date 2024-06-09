t = int(input())
input()
for X in range(t):
    n = int(input())
    print(n - 1)
    for i in range(n - 1):
        print(0, i)
    if X == t - 1:
        break
    input()

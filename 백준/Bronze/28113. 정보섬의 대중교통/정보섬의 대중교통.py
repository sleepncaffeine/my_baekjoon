n, a, b = map(int, input().split())
if n > b:
    print("Bus")
elif a == b:
    print("Anything")
elif a > b:
    print("Subway")
else:
    print("Bus")

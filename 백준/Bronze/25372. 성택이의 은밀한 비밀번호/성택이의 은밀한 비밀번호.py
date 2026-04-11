n = int(input())
for _ in range(n):
    s = input()
    if len(s) >= 6 and len(s) <= 9:
        print("yes")
    else:
        print("no")

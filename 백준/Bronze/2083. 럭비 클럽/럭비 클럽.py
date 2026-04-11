while True:
    (
        a,
        b,
        c,
    ) = input().split()
    b, c = int(b), int(c)
    if a == "#" and b == 0 and c == 0:
        break
    if b <= 17 and c < 80:
        print(a, "Junior")
    else:
        print(a, "Senior")

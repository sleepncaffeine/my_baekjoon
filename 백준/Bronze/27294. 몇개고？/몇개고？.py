t, s = map(int, input().split())
if s or not (t >= 12 and t <= 16):
    print(280)
elif (t >= 12 and t <= 16) and not s:
    print(320)

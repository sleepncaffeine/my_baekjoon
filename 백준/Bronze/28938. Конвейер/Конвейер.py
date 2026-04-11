n = int(input())
seq = list(map(int, input().split()))


if sum(seq) < 0:
    print("Left")
elif sum(seq) > 0:
    print("Right")
else:
    print("Stay")

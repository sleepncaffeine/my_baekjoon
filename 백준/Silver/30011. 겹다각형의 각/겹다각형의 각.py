n = int(input())
T = list(map(int, input().split()))

angle1 = 180 * (T[0] - 2)
angle2 = sum(T[1:]) * 180

print(angle1 + angle2)

n = int(input())
str = input()

for i in range(n):
    same = 0
    diff = 0
    for j in range(i + 1):
        if str[j] == str[n - i - 1 + j]:
            same += 1
        else:
            diff += 1
    if diff == 1:
        print("YES")
        exit()

print("NO")

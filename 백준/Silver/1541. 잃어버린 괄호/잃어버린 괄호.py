s = input()

numbers = []
operators = []

num = ""
for c in s:
    if c.isdigit():
        num += c
    else:
        numbers.append(int(num))
        operators.append(c)
        num = ""
numbers.append(int(num))

ans = numbers[0]

flag = False
for i in range(len(operators)):
    if operators[i] == "-":
        flag = True
    if flag:
        ans -= numbers[i + 1]
    else:
        ans += numbers[i + 1]

print(ans)

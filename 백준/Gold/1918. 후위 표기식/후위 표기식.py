exp = input()
res = ""
stack = []

for ch in exp:
    if ch.isupper():
        res += ch
    else:
        if ch == "(":
            stack.append(ch)
        elif ch in "+-":
            while stack and stack[-1] != "(":
                res += stack.pop()
            stack.append(ch)
        elif ch in "*/":
            while stack and stack[-1] in "*/":
                res += stack.pop()
            stack.append(ch)
        elif ch == ")":
            while stack and stack[-1] != "(":
                res += stack.pop()
            stack.pop()  # pop "("

while stack:
    res += stack.pop()

print(res)

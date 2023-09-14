from collections import deque

t = int(input())

for _ in range(t):
    bracket = deque(input())
    stack = []
    while bracket:
        p = bracket.popleft()
        if p == "(":
            stack.append(p)
        else:
            if not stack:
                print("NO")
                break
            else:
                stack.pop()
    else:
        if stack:
            print("NO")
        else:
            print("YES")

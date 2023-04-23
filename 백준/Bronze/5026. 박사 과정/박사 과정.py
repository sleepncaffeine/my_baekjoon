t = int(input())
for _ in range(t):
    question = input().split("+")
    if len(question) == 1:
        print("skipped")
    else:
        print(int(question[0]) + int(question[1]))

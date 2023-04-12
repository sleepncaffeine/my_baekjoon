N, K = map(int, input().split())
students = [[0,0] for _ in range(6)]
for _ in range(N):
    S, Y = map(int, input().split())
    students[Y-1][S] += 1
answer = 0
for grade in students:
    for gender in grade:
        answer += gender // K
        if gender % K:
            answer += 1
print(answer)

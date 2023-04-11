n = int(input())
clas = [] # 학생별 12345학년 속했었던 반
same = [0] * n # 행학생이 열 학생과 같은 반이었는가
for i in range(n):
    clas.append(list(map(int, input().split())))
    same[i] = [0] * n

for i in range(5): # i학년
    for j in range(n): # j번 i학년
        for k in range(j + 1, n): # k번의 i학년을
            # j번과 k번이 i학년 때 같은 반
            if clas[j][i] == clas[k][i]:
                # same=1.
                same[k][j] = 1
                same[j][k] = 1
                # += 1하면 같은반이었던 횟수 same에

cnt = [] # 학생별 같은 반이였던 학생수
for s in same:
    cnt.append(s.count(1))
print(cnt.index(max(cnt)) + 1)
N, B = map(int, input().split())
mat = []
for _ in range(N):
    mat.append(list(map(int, input().split())))


def matmul(a, b):
    res = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                res[i][j] += a[i][k] * b[k][j]
            res[i][j] %= 1000
    return res


def div_conq(a, b):
    if b == 1:
        return a
    else:
        temp = div_conq(a, b // 2)
        if b % 2 == 0:
            return matmul(temp, temp)
        else:
            return matmul(matmul(temp, temp), a)


res = div_conq(mat, B)

for row in res:
    for col in row:
        print(col % 1000, end=" ")
    print()

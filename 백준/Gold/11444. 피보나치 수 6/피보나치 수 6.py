N = int(input())
mat = [[1, 1], [1, 0]]


def matmul(a, b):
    res = [[0] * 2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                res[i][j] += a[i][k] * b[k][j]
            res[i][j] %= 1000000007
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


res = div_conq(mat, N)

print(res[0][1] % 1000000007)

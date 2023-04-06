import sys
from typing import List

mod = 1000000009

#knight dir
dx=[-2,-1,1,2]
dy=[1,0,0,1]

#operator overload for matmul
def matmul(x: List[List[int]], y: List[List[int]]) -> List[List[int]]:
    n = len(x)
    z = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                z[i][j] += x[i][k] * y[k][j]
                z[i][j] %= mod
    return z

def make(n: int) -> List[List[int]]:
    def onsq(cond: int, col: int, row: int) -> bool:
        return bool(cond & (1 << (n*col + row)))
    
    def okay(cond: int, next: int) -> bool:
        for i in range(n):
            if not onsq(next, 0, i):
                continue
            for j in range(4):
                if i + dx[j] < 0 or i + dx[j] >= n:
                    continue
                if onsq(cond, dy[j], i + dx[j]):
                    return False
        return True

    conditions = (1 << n * 2)
    injup = [[0] * conditions for _ in range(conditions)]

    for i in range(conditions):
        for j in range(1 << n):
            if okay(i, j):
                k = (i >> n) | (j << n)
                injup[i][k] = 1
    return injup

def pow(a: List[List[int]], x: int) -> List[List[int]]:
    n = len(a)
    res = [[0] * n for _ in range(n)]
    for i in range(n):
        res[i][i] = 1
    while x > 0:
        if x % 2:
            res = matmul(res, a)
        a = matmul(a, a)
        x //= 2
    return res

def main() -> None:
    t = int(input())
    for x in range(t):
        n, m = map(int, input().split())
        injup = make(n)
        res = pow(injup, m)
        s = sum(res[0][i] for i in range(1 << n * 2)) % mod
        print(s)

if __name__ == "__main__":
    main()

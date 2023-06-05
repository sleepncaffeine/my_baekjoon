def count_squares(n, m):
    if n == m:
        return 1
    elif n > m:
        return 1 + count_squares(n - m, m)
    else:
        return 1 + count_squares(n, m - n)


n, m = map(int, input().split())
print(count_squares(n, m))

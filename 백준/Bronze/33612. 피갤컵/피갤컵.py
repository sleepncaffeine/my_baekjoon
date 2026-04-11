n = int(input())

tot = (2024 * 12 + 8) + (n - 1) * 7
y = (tot - 1) // 12
m = (tot - 1) % 12 + 1
print(y, m)

n = int(input())
t = [0] * (n + 1)
p = [0] * (n + 1)
for i in range(1, n + 1):
    t[i], p[i] = map(int, input().split())

dp = [0] * (n + 1)

for i in range(1, n + 1):
    if i + t[i] - 1 <= n:
        dp[i + t[i] - 1] = max(dp[i + t[i] - 1], dp[i - 1] + p[i])
    dp[i] = max(dp[i], dp[i - 1])

print(dp[n])
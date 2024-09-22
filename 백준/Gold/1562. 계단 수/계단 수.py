MOD = int(1e9)
PWR = 1 << 10

n = int(input())

dp = [[[0 for _ in range(PWR)] for _ in range(10)] for _ in range(n)]

ans = 0

for i in range(1, 10):
    dp[0][i][1 << i] = 1

for i in range(1, n):
    for j in range(10):
        for k in range(PWR):
            if j > 0:
                dp[i][j][k | (1 << j)] += dp[i - 1][j - 1][k]
            if j < 9:
                dp[i][j][k | (1 << j)] += dp[i - 1][j + 1][k]

            dp[i][j][k | (1 << j)] %= MOD

for i in range(10):
    ans += dp[n - 1][i][(PWR) - 1]
    ans %= MOD

print(ans)

n = int(input())
nums = list(map(int, input().split()))

dp = [[0] * 2 for _ in range(n)]

ans = nums[0]

for i in range(n):
    dp[i][0] = nums[i]
    if i == 0:
        continue
    dp[i][0] = max(dp[i - 1][0] + nums[i], nums[i])
    dp[i][1] = max(dp[i - 1][0], dp[i - 1][1] + nums[i])
    ans = max(ans, dp[i][0], dp[i][1])

print(ans)

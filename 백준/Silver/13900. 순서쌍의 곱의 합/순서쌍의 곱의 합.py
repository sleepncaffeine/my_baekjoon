n = int(input())
nums = list(map(int, input().split()))
prefix = [0] * (n + 1)
prefix[0] = nums[0]
for i in range(1, n):
    prefix[i] = prefix[i - 1] + nums[i]

res = 0

for i in range(n):
    res += nums[i] * (prefix[n - 1] - prefix[i])

print(res)

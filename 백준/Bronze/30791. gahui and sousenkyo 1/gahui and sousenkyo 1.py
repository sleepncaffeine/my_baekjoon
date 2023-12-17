nums = list(map(int, input().split()))

cnt = 0
for num in nums[1:]:
    if nums[0] - num <= 1000:
        cnt += 1

print(cnt)
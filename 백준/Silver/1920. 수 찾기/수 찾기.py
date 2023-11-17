n = int(input())
nums = list(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))

nums.sort()

for i in targets:
    l = 0
    r = n - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == i:
            print(1)
            break
        elif nums[mid] > i:
            r = mid - 1
        else:
            l = mid + 1
    else:
        print(0)
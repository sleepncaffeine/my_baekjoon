n, m = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()


def dfs(nums, path, depth):
    if depth == m:
        print(*path)
        return
    for i in range(n):
        if nums[i] not in path:
            path.append(nums[i])
            dfs(nums, path, depth + 1)
            path.pop()


dfs(nums, [], 0)

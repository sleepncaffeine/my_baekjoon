n, m = map(int, input().split())
trees = list(map(int, input().split()))


def binary_search(trees, m):
    start = 0
    end = max(trees)
    while start <= end:
        mid = (start + end) // 2
        total = 0
        for tree in trees:
            if tree > mid:
                total += tree - mid
        if total >= m:
            start = mid + 1
        else:
            end = mid - 1
    return end


print(binary_search(trees, m))
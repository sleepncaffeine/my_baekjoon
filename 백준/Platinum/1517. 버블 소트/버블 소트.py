import sys

input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))
res = 0


def merge_sort(arr):
    global res
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])
    left = right = 0
    merged_arr = []
    while left < len(left_arr) and right < len(right_arr):
        if left_arr[left] <= right_arr[right]:
            merged_arr.append(left_arr[left])
            left += 1
        else:
            merged_arr.append(right_arr[right])
            right += 1
            res += len(left_arr) - left
    merged_arr += left_arr[left:]
    merged_arr += right_arr[right:]
    return merged_arr


merge_sort(arr)
print(res)

n = int(input())
cross = list(map(int, input().split()))

left = list(map(int, input().split()))

right = list(map(int, input().split()))

prefix_left = [0] * n
prefix_right = [0] * n

for i in range(1, n):
    prefix_left[i] = prefix_left[i - 1] + left[i - 1]
    prefix_right[i] = prefix_right[i - 1] + right[i - 1]

# print(prefix_left)
# print(prefix_right)

min_idx = -1
min_val = float("inf")

for i in range(n):
    len_left = prefix_left[i]
    len_right = prefix_right[n - 1] - prefix_right[i]
    len_cross = cross[i]
    total = len_left + len_right + len_cross
    if total < min_val:
        min_val = total
        min_idx = i

print(min_idx + 1, min_val)

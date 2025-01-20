s1, s2, s3 = map(int, input().strip().split())
a1 = [i for i in range(1, 1 + s1)]
a2 = [i for i in range(1, 1 + s2)]
a3 = [i for i in range(1, 1 + s3)]
l = [a + b + c for a in a1 for b in a2 for c in a3]
arr = [0] * 81

for i in l:
    arr[i] += 1

print(arr.index(max(arr)))

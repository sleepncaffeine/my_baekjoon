n = int(input())
arr1 = list(range(1, n + 1))

while len(arr1) != 1:
    arr2 = []
    for a in arr1[1::2]:
        arr2.append(a)

    arr1 = arr2

print(arr1[0])

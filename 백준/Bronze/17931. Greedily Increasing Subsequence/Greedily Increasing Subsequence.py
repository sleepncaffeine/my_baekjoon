n = int(input())
nums = list(map(int, input().split()))

gis = []
now = -1

for num in nums:
    if num > now:
        now = num
        gis.append(num)

print(len(gis))
print(" ".join(map(str, gis)))

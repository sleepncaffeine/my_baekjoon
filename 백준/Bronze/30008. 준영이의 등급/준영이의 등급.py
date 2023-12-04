n, k = map(int, input().split())
arr = list(map(int, input().split()))
grades = []
for num in arr:
    percent = num * 100 // n
    if 0 <= percent <= 4:
        grades.append(1)
    elif 5 <= percent <= 11:
        grades.append(2)
    elif 12 <= percent <= 23:
        grades.append(3)
    elif 24 <= percent <= 40:
        grades.append(4)
    elif 41 <= percent <= 60:
        grades.append(5)
    elif 61 <= percent <= 77:
        grades.append(6)
    elif 78 <= percent <= 89:
        grades.append(7)
    elif 90 <= percent <= 96:
        grades.append(8)
    else:
        grades.append(9)

print(*grades)

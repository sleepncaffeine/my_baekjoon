numbers = []
for i in range(9):
    numbers.append(int(input()))
M = max(numbers)
print(M)
print(numbers.index(M)+1)
import sys

print = sys.stdout.write

n = list(map(int, input()))

n.sort(reverse=True)

for i in n:
    print(str(i))

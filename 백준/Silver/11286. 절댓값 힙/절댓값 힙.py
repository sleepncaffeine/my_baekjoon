from queue import PriorityQueue
import sys

input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
q = PriorityQueue()

for _ in range(n):
    x = int(input())
    if x == 0:
        if q.empty():
            print("0\n")
        else:
            print(f"{q.get()[1]}\n")
    else:
        q.put((abs(x), x))
